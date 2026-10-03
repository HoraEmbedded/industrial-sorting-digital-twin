# PLC architecture

Target controller: Siemens S7-1200, CPU 1214C DC/DC/DC (project name `PLC_Sorting`), simulated with S7-PLCSIM and linked to the Factory I/O scene Sorting by Height (Advanced).

## Naming conventions

| Element | Convention | Example |
| --- | --- | --- |
| Input tag from Factory I/O | `I_` + Factory I/O tag name in PascalCase | `I_AtTurntableEntry` |
| Output tag to Factory I/O | `Q_` + Factory I/O tag name in PascalCase | `Q_EntryConveyor` |
| Function block, function | `FB_`, `FC_` + PascalCase | `FB_ModeManager` |
| Global data block | `DB_` + PascalCase | `DB_Machine` |
| PLC data type | `UDT_` + PascalCase | `UDT_ActuatorCmd` |
| Instance data block | block name + `_DB` | `FB_ModeManager_DB` |
| Block interface | `i_` input, `o_` output, `io_` in/out, `s_` static, `t_` temp | `i_StopNC` |
| Watch table | `WT_` + PascalCase | `WT_Mode` |

Design rules:

- Tags mirror the Factory I/O tag names, so the PLC and the scene stay in sync by name.
- No memory (M) bits for program state. State lives in `DB_Machine` or in FB static variables.
- Every `Q_` output is written in exactly one place: `FC_Outputs`.
- Comments are written in English.

## Signal polarity

| Signal | Wiring | Value at rest |
| --- | --- | --- |
| `I_Start` | Normally open | FALSE |
| `I_Stop` | Normally closed | TRUE |
| `I_EmergencyStop` | Normally closed | TRUE (healthy) |
| `I_Reset` | Normally open | FALSE |
| `I_Auto`, `I_Manual` | Two-position selector, one contact each | One of them is TRUE |

## Program structure

| Block | Role |
| --- | --- |
| `OB1` Main | Calls the blocks below, in this order |
| `FC9000` MHJ-PLC-Lab-Function-S71200 | Link with S7-PLCSIM, supplied with the Factory I/O template. Must stay first. |
| `FB_ModeManager` | Auto and Manual selection, Start, Stop, emergency stop fault latch |
| `FB_SortingLogic` | Sorting sequence, one box at a time (see sorting-sequence.md) |
| `FC_Outputs` | Safety gating and writing of all `Q_` outputs, lamps, counter display |
| `DB_Machine` | Machine status, actuator commands, counters |
| `UDT_ActuatorCmd` | One bit per actuator command |

## Operating modes

- Auto: Start launches the cycle (`Run`). Stop requests a stop at the end of the current cycle: `Run` drops when `CycleIdle` is TRUE.
- Manual: `Run` is always FALSE. Actuators follow `DB_Machine.ManCmd`, written from a watch table, for commissioning.
- Emergency stop: immediate. All actuators go FALSE and `Fault` is latched. After releasing the button, Reset clears `Fault`, then Start is required to run again.

## Output gating (FC_Outputs)

`Enable = I_EmergencyStop AND NOT Fault`

For each actuator X: `Q_X = Enable AND ((Run AND AutoCmd.X) OR (ManualMode AND ManCmd.X))`

Lamps: green and start light follow `Run`. Red and stop light follow NOT `Run`. Yellow is on when `Fault` or `ManualMode`. The reset light is on when `Fault` is latched and the emergency stop is released.


## FB_SortingLogic interface

| Direction | Name | Type | Role |
| --- | --- | --- | --- |
| Input | `i_Run` | Bool | Machine running in Auto |
| Input | `i_StopPending` | Bool | Stop requested, no new cycle may start |
| Input | `i_ClearCounters` | Bool | Zero the counters |
| Input | `i_ExitIdleHigh` | Bool | TRUE if the exit sensors are TRUE with no box |
| Input | `i_AtEntry`, `i_AtLoadPosition`, `i_AtTurntableEntry`, `i_AtUnloadPosition`, `i_HighBox` | Bool | Entry, turntable and light curtain sensors |
| Input | `i_AtLeftEntry`, `i_AtRightEntry`, `i_AtLeftExit`, `i_AtRightExit` | Bool | Exit conveyor sensors |
| Output | `o_CycleIdle` | Bool | No cycle in progress, no box in transit |
| Output | `o_Step` | Int | Current step, for monitoring |
| InOut | `io_Cmd` | `UDT_ActuatorCmd` | Automatic actuator commands |
| InOut | `io_CountLeft`, `io_CountRight`, `io_CountTotal` | Int | Counters |
| Input | `i_AtFront` | Bool | Queue sensor in front of the turntable |
| Input | `i_CenterTime` | Time | Centering delay after the box reaches the turntable center |

## DB_Machine additions

| Name | Type | Role |
| --- | --- | --- |
| `SortStep` | Int | Current step of the sorting sequence |
| `ClearCounters` | Bool | Set by OB1 when Reset is pressed in Manual mode |
| `ExitIdleHigh` | Bool | Configuration, value measured in scene-behavior.md (E09, E10) |


## Known limitation

In Manual mode, a command left TRUE in `ManCmd` restarts the actuator after a Reset. Set the commands back to FALSE before resetting.