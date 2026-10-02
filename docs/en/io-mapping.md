# I/O mapping

Single source of truth for the link between Factory I/O and the PLC. Addresses are read from the Factory I/O driver page (driver: Siemens S7-PLCSIM). Some tags were not mapped automatically by the driver and were added by hand in the scene.

## Hardware addressing

The on-board DI 14/DQ 10 of the CPU is moved to start address 100, so it never overlaps the process image area written by Factory I/O. The compiler warning "Inputs or outputs are used that do not exist in the configured hardware" is expected with this approach.

## Inputs (Factory I/O sensors to PLC)

| PLC tag | Factory I/O tag | Type | Address | Notes |
| --- | --- | --- | --- | --- |
| `I_atBack` | at back | Bool | %I2.1 | Role to confirm in scene-behavior.md |
| `I_atEntry` | at entry | Bool | %I0.0 | Role to confirm |
| `I_atFront` | At front | Bool | %I0.6 | Role to confirm |
| `I_atLeftEntry` | At left entry | Bool | %I1.0 | Role to confirm |
| `I_atLeftExit` | At left exit | Bool | %I1.2 | Role to confirm |
| `I_atLoadPosition` | At load position | Bool | %I0.4 | Role to confirm |
| `I_atRightEntry` | At right entry | Bool | %I0.7 | Role to confirm |
| `I_atRightExit` | At right exit | Bool | %I1.1 | Role to confirm |
| `I_atTurntableEntry` | At turntable entry | Bool | %I0.3 | Role to confirm |
| `I_atUnloadPosition` | At unload position | Bool | %I0.5 | Role to confirm |
| `I_Auto` | Auto | Bool | %I1.7 | Selector in Auto |
| `I_Manual` | Manual | Bool | %I2.2 | Selector in Manual, TRUE at rest in the scene |
| `I_EmergencyStop` | Emergency stop | Bool | %I1.6 | Normally closed, TRUE when healthy |
| `I_HighBox` | High box | Bool | %I0.2 | Light curtain, high box |
| `I_LowBox` | Low box | Bool | %I0.1 | Light curtain, low box |
| `I_Reset` | Reset | Bool | %I1.4 | Normally open pushbutton |
| `I_Start` | Start | Bool | %I1.3 | Normally open pushbutton |
| `I_Stop` | Stop | Bool | %I1.5 | Normally closed, TRUE at rest |

## Outputs (PLC to Factory I/O actuators)

| PLC tag | Factory I/O tag | Type | Address | Notes |
| --- | --- | --- | --- | --- |
| `Q_Counter` | Counter | DInt | %QD30 | Counter display on the operator panel |
| `Q_Emit` | Emitter 1 (Emit) | Bool | %Q1.7 | Box emitter, behavior to confirm |
| `Q_EntryConveyor` | Entry conveyor | Bool | %Q0.1 | |
| `Q_FeederConveyor` | Feeder conveyor | Bool | %Q0.0 | |
| `Q_GreenIndicator` | Green indicator | Bool | %Q0.7 | Tower light |
| `Q_LeftConveyor` | Left conveyor | Bool | %Q0.5 | |
| `Q_Load` | Load | Bool | %Q0.2 | Turntable, role to confirm |
| `Q_RedIndicator` | Red indicator | Bool | %Q1.1 | Tower light |
| `Q_RemoverLeft` | Remover left | Bool | %Q1.5 | Behavior to confirm |
| `Q_RemoverRight` | Remover right | Bool | %Q1.6 | Behavior to confirm |
| `Q_ResetLight` | Reset light | Bool | %Q1.3 | Lamp of the Reset pushbutton |
| `Q_RightConveyor` | Right conveyor | Bool | %Q0.6 | |
| `Q_StartLight` | Start light | Bool | %Q1.2 | Lamp of the Start pushbutton |
| `Q_StopLight` | Stop light | Bool | %Q1.4 | Lamp of the Stop pushbutton |
| `Q_Turn` | Turn | Bool | %Q0.4 | Turntable, role to confirm |
| `Q_Unload` | Unload | Bool | %Q0.3 | Turntable, role to confirm |
| `Q_YellowIndicator` | Yellow indicator | Bool | %Q1.0 | Tower light |

## Tags not used by the PLC

The Factory I/O system tags (Paused, Reset, Running, Time Scale, Camera Position, Pause, Run) control the simulator, not the machine. `FACTORY I/O (Running)` is mapped to %I2.0 in the scene but unused by the PLC. The unnamed sensor slots are unused.