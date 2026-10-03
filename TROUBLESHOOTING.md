# Troubleshooting Log

This document records every difficulty encountered during the project, even the smallest ones, and how they were solved. The goal is to keep a full history of the problem solving process for the portfolio and for future reference.

## Purpose

- Keep a trace of every issue, no matter how small
- Document every attempt, not only the successful one
- Identify root causes and lessons learned
- Build a reusable knowledge base for future automation projects

## Format

Each entry follows this template:

```text
### YYYY-MM-DD - Short title

- Context: where and when the issue appeared
- Symptom: what was observed
- Attempts:
  1. First attempt and result
  2. Second attempt and result
  3. ...
- Root cause: the actual cause once identified
- Solution: what finally fixed it
- Lesson learned: what to remember for next time
```

## Entries

<!-- Add new entries at the top of this section, most recent first -->

### 2026-10-03 - Memory leakage and initialization failure during continuous loop re-architecture

- Context: Step 3.2 & 3.4 (Pipelined cycle transition mapping) inside `FB_SortingLogic` in TIA Portal V18.
- Symptom: Upon implementing the direct transition from Step 5 to Step 1, the second box automatically inherited the height parameter of the first box and skipped the centering delay timer execution.
- Attempts:
  1. Kept the height latch and entry seen resets mapped to `EQ(s_Step, 0)`. Result: Failed instantly because Step 0 is completely bypassed during continuous pipelined execution loops, leaving old states active.
- Root cause: Sequential bypass. By design, a pipelined loop skips the default idle state (Step 0) to maintain flow velocity. Any latch reset depending strictly on Step 0 becomes dead code, causing a permanent memory leak from cycle to cycle.
- Solution: Shifted the `R1` (Reset) triggers for both the `height latch` and `Entry seen latch` networks to evaluate `EQ(s_Step, 1)`. This guarantees that memory blocks are forced to FALSE at the exact microsecond a new part emission is executed, isolating each part run.
- Lesson learned: When eliminating idle steps to establish pipeline operations, relocate the sequence initialization commands to the new entry point of the loop (Step 1) rather than the standard idle state.


### 2026-10-03 - Sequence freezing at step 4 and random sorting during loop execution due to transient step behavior

- Context: Step 3.5 (Infinite loop activation) of the sorting logic implementation inside `FB_SortingLogic` in TIA Portal V18 and Factory I/O.
- Symptom: The first box was sorted perfectly, but the sequence then froze at `SortStep = 4`. The turntable remained rotated at 90°, and the main entry conveyor stopped. When attempting to force the continuous loop, the system started dispatching both low and high boxes completely at random to either side.
- Attempts:
  1. Implemented a parallel reset branch using `EQ(s_Step, 6)` on the `R1` input of the height and entry latches. Result: The infinite loop started running, but the sorting became completely random because the high-speed loop cleared the height memory `#s_SeenHigh` while the box was still being discharged at Step 4, causing the rollers to stop or misread the box type.
  2. Reverted the reset condition strictly to `EQ(s_Step, 0)` to preserve memory through the discharge phase. Result: The system fell back to the initial symptom where the second box stopped dead right before the turntable because Step 0 was skipped too fast for the latches to register the reset command.
- Root cause: A classic PLC race condition involving microsecond transient steps. Because TIA Portal processes code sequentially from top to bottom, the transition from Step 6 to 0 and immediately from Step 0 to 1 occurred within a single PLC scan cycle. The upper networks never "saw" `s_Step` equal to 0, leaving the entry latch permanently stuck at TRUE. This forced the filtering timer to expire instantly on the second box, while the late reset at Step 6 cut the actuator power mid-discharge.
- Solution: Restructured the reset logic for the memory blocks. Configured the `R1` input of `#s_SeenHigh` (Height latch) to clear on `EQ(s_Step, 0) OR EQ(s_Step, 1)` to ensure it wipes clean the moment a new cycle generates a box. Modified the transition network T0 to 1 (Network 13) by adding a Normally Closed contact `NOT s_AtEntrySeen` in series, mathematically forcing the state machine to remain at Step 0 for at least one full scan cycle until the background latches safely clear out.
- Lesson learned: Never assume a transient step (like Step 0 in a loop) stays active long enough to clear latches in upper networks. Interlock the transition leaving that step with a Normally Closed contact of the latch itself to guarantee the PLC scan cycle has safely processed the memory reset before advancing.


### 2026-10-03 - Turntable premature rotation and box blocking due to hardware-space mismatch and memory conflicts

- Context: Step 3.5 (First automatic trial) of the sorting logic implementation inside `FB_SortingLogic` in TIA Portal V18 and Factory I/O.
- Symptom: The system kept skipping steps immediately. The turntable rotated to 90° completely empty before the box could even reach it. The box ended up permanently blocked right before the plateau flanc, the main conveyor stopped, and exit lines ran indefinitely in the air while the sequence stood frozen at Step 4.
- Attempts:
  1. Checked initial sensor values at rest to find a potential polarity inversion, but all physical levels were clean and coherent.
  2. Suspected a premature trigger from the edge of the box on `I_atTurntableEntry` and added a standard `TON` timer directly in the transition network (Network 11). Result: The box completely overshot the plateau and fell off into the void because the timer instanced memory `#s_TonEmit` was shared with the emitter network, causing critical data overwriting.
  3. Switched the timer to a dedicated multi-instance variable `#s_TonCenter` and added a Normally Open contact on the actuator command (`Q_Load`) to cut the power on sensor detection. Result: The box stopped dead before even hitting the plateau because a Normally Open contact was used instead of a Normally Closed one.
  4. Implemented a specific sequence latch (`s_AtEntrySeen`) and separated the logic into distinct networks, but the sequence still jumped to Step 4 at startup because the calculation networks were inserted right in the middle of the sequential décroissant transition block, breaking the execution scanning order.
- Root cause: Multiple combined factors. First, a space-vs-time architectural error: `I_atTurntableEntry` is a fixed sensor at the edge of the entry line, not a centering sensor on the plateau, making direct transition mapping impossible without a shift delay. Second, severe memory collisions occurred due to an instance-sharing typo on the standard timer (`#s_TonEmit`). Finally, placing the auxiliary latch and timer networks inside the sequential T6-to-T0 transition block forced TIA Portal to cascade `MOVE` operations within a single PLC program scan cycle.
- Solution: Created a clean independent `IEC_TIMER` static variable (`s_TonCenter`) linked to a runtime parameter `i_CenterTime` (set to `T#2s`). Re-architectured the block networks by moving the "Entry seen latch" and "Center timer" networks cleanly above the transition stack (right after Network 6). Rewrote Network 11 to evaluate `s_TonCenter.Q`, and corrected the `Q_Load` command network to use a proper Normally Closed interlock on the center sensor.
- Lesson learned: Never share instance data blocks or timers across separate networks. Sequential transitions in LAD-coded Grafcets must remain perfectly continuous from T6 to T0; any auxiliary latch or filtering timer must be computed *before* evaluating the state machine transitions to prevent microsecond step-skipping.


### 2026-10-02 - Start button failing to latch Run due to temporary variable inversion

- Context: Commissioning Mission 6 (Advanced sorting scene) inside the `FB_ModeManager` block in TIA Portal V18.
- Symptom: The `"DB_Machine".Run` variable refused to pass to TRUE, and the green indicator never turned on, even when keeping the physical Start button fully pressed. All safety conditions (`Fault = FALSE`, `Stop = TRUE`, `EmergencyStop = TRUE`) were perfectly met.
- Attempts:
  1. Monitored the `WT_Mode` watch table to verify the physical input `I_Start` (%I1.3), which correctly changed from FALSE to TRUE when pressed.
  2. Checked if the `StopPending` latch or static edge memories were blocking the execution, but they were properly cleared.
  3. Inspected the internal logic of `FB_ModeManager` using the online monitoring glasses.
- Root cause: Typo in the Network 3 assignment. The output coil of the Start button edge detection network was mistakenly assigned to the temporary variable `#t_ResetPulse` instead of `#t_StartPulse`. This caused the Start button to fire a reset pulse instead of a start pulse, leaving the Run SR latch with no input signal.
- Solution: Double-clicked the coil in Network 3 of `FB_ModeManager` and changed the variable name to `#t_StartPulse`, then compiled and downloaded the software modification to PLCSIM.
- Lesson learned: Always double-check temporary pulse variable names (`#t_...Pulse`) in edge detection networks, as a single typo can cause a command button to trigger an completely opposite action.


### 2026-10-02 - Permanent blinking of variables and impossible reset due to I/O address conflict

- Context: Commissioning Mission 6 (Advanced sorting scene) using TIA Portal V18, S7-PLCSIM, and Factory I/O.
- Symptom: The `AutoMode` variable was rapidly blinking between TRUE and FALSE. The `Reset light` and the red/yellow indicators stayed permanently on. Pressing the `Start` or `Reset` buttons had no effect.
- Attempts:
  1. Switched the physical selector to Auto in the 3D scene, but variables kept oscillating and the safety fault could not be cleared.
  2. Analyzed the Factory I/O driver page and noticed that the active sensors used the exact same address range (%I0.0 to %I1.5) as the CPU's default integrated inputs.
- Root cause: Hardware address overlap. The default on-board digital inputs/outputs of the S7-1200 CPU occupied the process image area from byte 0 to 1. The virtual CPU forced these addresses to 0 (unwired) while Factory I/O forced them to 1, causing a conflict and a rapid signal oscillation at every PLC scan cycle.
- Solution: Opened the CPU Device Configuration in TIA Portal, changed the integrated DI/DQ Start address from 0 to 100, chose "Do not change tags" to preserve the simulation mapping, performed a full hardware and software compilation, and downloaded the update to PLCSIM.
- Lesson learned: Always shift the CPU's integrated physical E/S start addresses to a higher offset (e.g., 100) when working with Factory I/O to completely free up the low-byte process image for simulation data.

### 2026-10-02
Symptom: compile warning "Inputs or outputs are used that do not exist in the configured hardware".
Cause: the Factory I/O addresses (I0.0 to I2.2, Q0.0 to Q1.7, QD30) are outside the on-board I/O of the CPU.
Resolution: expected with S7-PLCSIM co-simulation. The on-board I/O was moved to address 100 to avoid any overlap. Warning accepted.
Status: to be confirmed by test T01.

### 2026-09-30 - Main OB1 opened in SCL instead of LAD in TIA Portal

- Context: Mission 3, step 4, writing a minimal test program in OB1
- Symptom: The Main [OB1] block opened as text code (SCL), the LAD toolbar with contacts was missing, and the "Bit logic operations" panel showed text entries instead of contact icons
- Attempts:
  1. Tried to find the LAD contact toolbar in the ribbon, not present
  2. Searched the instructions panel for bit logic icons, only SCL entries appeared
  3. Checked online documentation and video tutorials to understand the difference between SCL and LAD blocks
- Root cause: The Main [OB1] block was created with SCL as its programming language. The language of a block is fixed at creation time in TIA Portal and determines which editor and which instruction set are available
- Solution: Created a new block in the project tree via Add new block, selected Function block or Organization block, and set the Language dropdown to LAD instead of SCL. Opened the new block and the graphical LAD editor appeared with the contact toolbar
- Lesson learned: In TIA Portal, the programming language of a block is chosen at creation time. LAD and SCL blocks coexist in the same project. Always check the Language field in the Add new block dialog before clicking OK

### 2026-09-28 - Factory I/O driver error "more than one instance of S7-PLCSIM has been detected"

- Context: Mission 3, step 4, connecting Factory I/O to PLCSIM via the Siemens S7-PLCSIM driver
- Symptom: Factory I/O displayed a red error message stating that more than one instance of S7-PLCSIM had been detected
- Attempts:
  1. Clicked CONNECT again in Factory I/O, same error
  2. Opened Windows Task Manager to inspect running processes
  3. Found multiple hidden S7-PLCSIM background processes left from previous sessions
- Root cause: PLCSIM was launched several times without the previous instance being shut down. The S7-PLCSIM driver requires exactly one running instance to bind to
- Solution: Closed every visible PLCSIM window, killed the remaining S7-PLCSIM processes in Windows Task Manager, restarted a single PLCSIM instance from TIA Portal, waited for the CPU to be in RUN, then clicked CONNECT in Factory I/O. The driver indicator turned green
- Lesson learned: Always ensure only one PLCSIM instance is running before connecting Factory I/O. Clean up zombie processes with the Task Manager. Always start PLCSIM first, then connect the driver

### 2026-09-28 - Difficulty establishing the full TIA Portal to PLCSIM to Factory I/O connection

- Context: Mission 3, step 4, end to end co-simulation test
- Symptom: The chain between TIA Portal, PLCSIM and Factory I/O did not connect on the first attempts, even with correct versions
- Attempts:
  1. Tried to connect PLCSIM to Factory I/O directly, failed
  2. Tried to start Factory I/O first, then PLCSIM, failed
  3. Followed a step by step YouTube tutorial on setting up the co-simulation, and reproduced the exact sequence
- Root cause: The connection procedure requires a strict order. TIA Portal project must compile first, PLCSIM must be started from TIA Portal, the PLC must be in RUN, only one PLCSIM instance must exist, then Factory I/O must be opened with the Siemens S7-PLCSIM driver selected, and only then can CONNECT be pressed
- Solution: Applied the strict sequence: compile in TIA Portal, start simulation from TIA Portal, download the program, put the CPU in RUN, verify a single PLCSIM instance, open Factory I/O, select the Siemens S7-PLCSIM driver, click CONNECT, verify the green indicator
- Lesson learned: Industrial co-simulation follows a strict startup sequence. Documenting that sequence in the project is more valuable than trying to remember it. This is the kind of procedure that belongs in a runbook for operators and commissioning engineers

### 2026-09-28 - PLC security settings dialog appears when adding a CPU in TIA Portal

- Context: Mission 3, step 4, adding a CPU 1214C to a new TIA Portal project
- Symptom: After validating the CPU selection, TIA Portal opened a dialog called "PLC security settings" asking for a password and a protection level
- Attempts:
  1. Considered setting a password, then realized it was not needed for local simulation
  2. Checked the purpose of each protection level in the dialog
- Root cause: Recent TIA Portal versions ask for security settings as soon as a new CPU is created, to comply with industrial cybersecurity requirements
- Solution: Unchecked "Protects the PLC configuration data", selected no protection in the following steps, and finished the wizard. The CPU was added without a password
- Lesson learned: In TIA Portal V15 and later, always expect the PLC security settings dialog. In local simulation, no protection is needed. In production, protection is mandatory


### 2026-09-28 - CPU 1214C DC/DC/DC appears as a catalog folder in TIA Portal

- Context: Mission 3, step 4, adding a CPU to a new TIA Portal project
- Symptom: In the "Add new device" dialog, CPU 1214C DC/DC/DC was displayed as a folder with several entries inside, not as a single clickable device
- Attempts:
  1. Tried to double click on the folder, nothing happened
  2. Checked the documentation online to understand the catalog structure
- Root cause: In TIA Portal, the CPU reference 1214C DC/DC/DC is a catalog node that contains several firmware versions. The user must expand the node and pick the desired firmware version
- Solution: Expanded the node and selected the firmware version V4.5 or later, then clicked OK
- Lesson learned: In TIA Portal, always expect the hardware catalog to be hierarchical. Expand nodes to see firmware versions. Pick the firmware that matches the target environment


### 2026-09-28 - TIA Portal V18 installation blocked by pending file rename operations

- Context: Installation of TIA Portal V18 on Windows
- Symptom: The installer kept asking for a restart before starting, and restarting did not solve it
- Attempts:
  1. Restarted the computer and launched Start.exe again, same prompt
  2. Ran Start.exe as administrator, same prompt
  3. Inspected the Windows registry to check pending operations
- Root cause: The registry key `PendingFileRenameOperations` in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SessionManager` contained entries left by a previous installer, which made Windows believe a restart was still pending
- Solution: Opened `regedit`, navigated to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SessionManager`, deleted the `PendingFileRenameOperations` value, then relaunched `Start.exe` as administrator without restarting
- Lesson learned: Before installing Siemens software, always check this registry key. It is a well known blocker for TIA Portal installers

### 2026-09-28 - License Manager version conflict with TIA Portal V18

- Context: Installation of TIA Portal V18 on Windows
- Symptom: The installer reported a version conflict with the existing Automation License Manager
- Attempts:
  1. Tried to continue the installation with the existing License Manager, blocked
  2. Checked the version requirement of TIA Portal V18
  3. Downloaded the latest Automation License Manager from the Siemens support site
- Root cause: TIA Portal V18 requires a more recent version of Automation License Manager than the one already installed
- Solution: Installed the latest Automation License Manager first, then resumed the TIA Portal installation successfully
- Lesson learned: Always install the latest Automation License Manager before a new TIA Portal version, and check the compatibility matrix on the Siemens support site

### 2026-09-28 - Repository bootstrap on Windows

- Context: Mission 1, repository initialization on Windows
- Symptom: None, entry created to validate the format
- Attempts:
  1. Created the repository locally
  2. Added the initial folder structure
  3. Made the first commit and pushed to GitHub
- Root cause: Not applicable, this is a template entry
- Solution: Not applicable
- Lesson learned: Always check `git status` before committing
