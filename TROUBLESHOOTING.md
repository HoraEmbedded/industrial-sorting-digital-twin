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

### 2026-01-01 - Main OB1 opened in SCL instead of LAD in TIA Portal

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
