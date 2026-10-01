# I/O mapping

Single source of truth for the link between Factory I/O and the PLC. Addresses are read from the Factory I/O driver page (driver: Siemens S7-PLCSIM).

## Hardware addressing

The on-board DI 14/DQ 10 of the CPU is moved to start address 100, so it never overlaps the process image area written by Factory I/O.

## Inputs (Factory I/O sensors to PLC)

| PLC tag | Factory I/O tag | Type | Address | Notes |
| --- | --- | --- | --- | --- |
| `I_AtBack` | At back | Bool | | Role to confirm in scene-behavior.md |
| `I_AtEntry` | At entry | Bool | | Role to confirm |
| `I_AtFront` | At front | Bool | | Role to confirm |
| `I_AtLeftEntry` | At left entry | Bool | | Role to confirm |
| `I_AtLeftExit` | At left exit | Bool | | Role to confirm |
| `I_AtLoadPosition` | At load position | Bool | | Role to confirm |
| `I_AtRightEntry` | At right entry | Bool | | Role to confirm |
| `I_AtRightExit` | At right exit | Bool | | Role to confirm |
| `I_AtTurntableEntry` | At turntable entry | Bool | | Role to confirm |
| `I_AtUnloadPosition` | At unload position | Bool | | Role to confirm |
| `I_Auto` | Auto | Bool | | Selector in Auto |
| `I_Manual` | Manual | Bool | | Selector in Manual, TRUE at rest in the scene |
| `I_EmergencyStop` | Emergency stop | Bool | | Normally closed, TRUE when healthy |
| `I_HighBox` | High box | Bool | | Light curtain, high box |
| `I_LowBox` | Low box | Bool | | Light curtain, low box |
| `I_Reset` | Reset | Bool | | Normally open pushbutton |
| `I_Start` | Start | Bool | | Normally open pushbutton |
| `I_Stop` | Stop | Bool | | Normally closed, TRUE at rest |

## Outputs (PLC to Factory I/O actuators)

| PLC tag | Factory I/O tag | Type | Address | Notes |
| --- | --- | --- | --- | --- |
| `Q_Counter` | Counter | Int | | Counter display on the operator panel |
| `Q_Emit` | Emitter 1 (Emit) | Bool | | Box emitter, behavior to confirm |
| `Q_EntryConveyor` | Entry conveyor | Bool | | |
| `Q_FeederConveyor` | Feeder conveyor | Bool | | |
| `Q_GreenIndicator` | Green indicator | Bool | | Tower light |
| `Q_LeftConveyor` | Left conveyor | Bool | | |
| `Q_Load` | Load | Bool | | Turntable, role to confirm |
| `Q_RedIndicator` | Red indicator | Bool | | Tower light |
| `Q_RemoverLeft` | Remover left | Bool | | Behavior to confirm |
| `Q_RemoverRight` | Remover right | Bool | | Behavior to confirm |
| `Q_ResetLight` | Reset light | Bool | | Lamp of the Reset pushbutton |
| `Q_RightConveyor` | Right conveyor | Bool | | |
| `Q_StartLight` | Start light | Bool | | Lamp of the Start pushbutton |
| `Q_StopLight` | Stop light | Bool | | Lamp of the Stop pushbutton |
| `Q_Turn` | Turn | Bool | | Turntable, role to confirm |
| `Q_Unload` | Unload | Bool | | Turntable, role to confirm |
| `Q_YellowIndicator` | Yellow indicator | Bool | | Tower light |

## Tags not used by the PLC

The Factory I/O system tags (Paused, Reset, Running, Time Scale, Camera Position, Pause, Run) control the simulator, not the machine. The unnamed sensor slots are unused.