# I/O mapping

Single source of truth for the link between Factory I/O and the PLC. Addresses are read from the Factory I/O driver page (driver: Siemens S7-PLCSIM). Some tags were not mapped automatically by the driver and were added by hand in the scene.

## Hardware addressing

The on-board DI 14/DQ 10 of the CPU is moved to start address 100, so it never overlaps the process image area written by Factory I/O. The compiler warning "Inputs or outputs are used that do not exist in the configured hardware" is expected with this approach.

## Inputs (Factory I/O sensors to PLC)

| PLC tag | Factory I/O tag | Type | Address | Notes |
| --- | --- | --- | --- | --- |
| `I_atBack` | at back | Bool | %I2.1 | Rear entrance conveyor sensor. Confirms a box has fully cleared the entry area. |
| `I_atEntry` | at entry | Bool | %I0.0 | Photocenter at the very beginning of the line. Detects box emergence. |
| `I_atFront` | At front | Bool | %I0.6 | Queue sensor right before the turntable. Prevents part collisions. |
| `I_atLeftEntry` | At left entry | Bool | %I1.0 | Confirms the box has successfully transitioned onto the Left exit conveyor. |
| `I_atLeftExit` | At left exit | Bool | %I1.2 | Normally Closed (NC). Drops to FALSE when a box reaches the left remover. |
| `I_atLoadPosition` | At load position | Bool | %I0.4 | Limit switch. TRUE when turntable is at 0° (aligned with entry). |
| `I_atRightEntry` | At right entry | Bool | %I0.7 | Confirms the box has successfully transitioned onto the Right exit conveyor. |
| `I_atRightExit` | At right exit | Bool | %I1.1 | Normally Closed (NC). Drops to FALSE when a box reaches the right remover. |
| `I_atTurntableEntry` | At turntable entry | Bool | %I0.3 | Center reflective sensor inside the turntable. Used for precise stopping. |
| `I_atUnloadPosition` | At unload position | Bool | %I0.5 | Limit switch. TRUE when turntable has completed its 90° clockwise rotation. |
| `I_Auto` | Auto | Bool | %I1.7 | Selector in Auto position. |
| `I_Manual` | Manual | Bool | %I2.2 | Selector in Manual position. TRUE at rest in the default scene layout. |
| `I_EmergencyStop` | Emergency stop | Bool | %I1.6 | Normally Closed (NC). TRUE when healthy, drops to FALSE when pressed. |
| `I_HighBox` | High box | Bool | %I0.2 | Top light curtain beam. Active (TRUE) only alongside LowBox for high boxes. |
| `I_LowBox` | Low box | Bool | %I0.1 | Bottom light curtain beam. Active (TRUE) for both low and high boxes. |
| `I_Reset` | Reset | Bool | %I1.4 | Normally Open (NO) pushbutton. Clears safety fault latches. |
| `I_Start` | Start | Bool | %I1.3 | Normally Open (NO) pushbutton. Triggers the cycle run latch. |
| `I_Stop` | Stop | Bool | %I1.5 | Normally Closed (NC). TRUE at rest, drops to FALSE to request a cycle stop. |

## Outputs (PLC to Factory I/O actuators)

| PLC tag | Factory I/O tag | Type | Address | Notes |
| --- | --- | --- | --- | --- |
| `Q_Counter` | Counter | DInt | %QD30 | Digital totalizer display unit located on the operator panel. |
| `Q_Emit` | Emitter 1 (Emit) | Bool | %Q1.7 | Pulse triggers box generation. Continuous TRUE spawns boxes sequentially. |
| `Q_EntryConveyor` | Entry conveyor | Bool | %Q0.1 | Drives the second section of the entry lane towards the turntable. |
| `Q_FeederConveyor` | Feeder conveyor | Bool | %Q0.0 | Drives the first entry section right beneath the box emitter. |
| `Q_GreenIndicator` | Green indicator | Bool | %Q0.7 | Stack light tower: Constant green indicates system is running active cycles. |
| `Q_LeftConveyor` | Left conveyor | Bool | %Q0.5 | Drives the left clearance exit lane. |
| `Q_Load` | Load | Bool | %Q0.2 | Runs internal turntable rollers forward to pull a box inside. |
| `Q_RedIndicator` | Red indicator | Bool | %Q1.1 | Stack light tower: Constant red indicates system is idle/stopped. |
| `Q_RemoverLeft` | Remover left | Bool | %Q1.5 | Active clearing device. Instantly deletes boxes at the left exit limit. |
| `Q_RemoverRight` | Remover right | Bool | %Q1.6 | Active clearing device. Instantly deletes boxes at the right exit limit. |
| `Q_ResetLight` | Reset light | Bool | %Q1.3 | Built-in blue/white lamp. Active when safety is tripped and waiting for Reset. |
| `Q_RightConveyor` | Right conveyor | Bool | %Q0.6 | Drives the right clearance exit lane. |
| `Q_StartLight` | Start light | Bool | %Q1.2 | Built-in green lamp inside the Start button. Follows the Run state. |
| `Q_StopLight` | Stop light | Bool | %Q1.4 | Built-in red lamp inside the Stop button. Active when cycle is offline. |
| `Q_Turn` | Turn | Bool | %Q0.4 | Swivels the turntable mechanism 90° clockwise. Returns home when FALSE. |
| `Q_Unload` | Unload | Bool | %Q0.3 | Runs internal turntable rollers backward to eject a box out to the left lane. |
| `Q_YellowIndicator` | Yellow indicator | Bool | %Q1.0 | Stack light tower: Active on safety Fault or when system is in Manual mode. |

## Tags not used by the PLC

The Factory I/O system tags (Paused, Reset, Running, Time Scale, Camera Position, Pause, Run) control the simulator, not the machine. `FACTORY I/O (Running)` is mapped to %I2.0 in the scene but unused by the PLC. The unnamed sensor slots are unused.
