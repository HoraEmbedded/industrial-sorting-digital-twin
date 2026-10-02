# Scene behavior

Observations of the Factory I/O scene Sorting by Height (Advanced), recorded in Manual mode by writing `DB_Machine.ManCmd` from the watch table `WT_Manual`. This document is the input for the sorting logic.

## Experiments

| ID | How | Record | Observation |
| --- | --- | --- | --- |
| E01 | Set `ManCmd.Emit` TRUE for 1 s, then FALSE | Does a box appear? One box per pulse, or continuous while TRUE? Which sensor switches first? | One box appears per single pulse. If held TRUE, boxes are generated continuously with a fixed spacing. The first sensor to switch TRUE is `I_AtEntry`. |
| E02 | Set `ManCmd.FeederConveyor`, then `ManCmd.EntryConveyor` TRUE | Order in which the sensors switch while a box travels | The sequence of activation as the box moves forward is: `I_AtEntry` -> `I_LowBox` / `I_HighBox` (height curtain) -> `I_AtFront` -> `I_AtTurntableEntry`. |
| E03 | Let one low box and one high box cross the light curtain | `I_LowBox` and `I_HighBox` for each box type, and for how long | **Low Box:** `I_LowBox` switches to TRUE, `I_HighBox` stays FALSE. **High Box:** Both `I_LowBox` and `I_HighBox` switch to TRUE simultaneously. Sensors stay TRUE during the whole transit time across the light curtain. |
| E04 | Empty turntable: set `ManCmd.Load`, `Unload` and `Turn`, alone and combined | Roller direction, rotation direction and angle, sensors that change | `Load` runs internal rollers forward (draws box inside). `Unload` runs rollers backward (pushes box outside). `Turn` rotates the table 90° clockwise. `I_AtLoadPosition` is TRUE at rest (aligned with entry). `I_AtUnloadPosition` is TRUE when fully turned 90°. |
| E05 | Box on the turntable: find the sequence that sends it to the left conveyor, then to the right one | Ordered list of commands and sensors | **Centering:** `Load=1` until `I_AtTurntableEntry=1`, then `Load=0`. **Rotation:** `Turn=1` until `I_AtUnloadPosition=1`. **To LEFT:** Set `Unload=1` and `LeftConveyor=1`. **To RIGHT:** Set `Load=1` and `RightConveyor=1`. Release all commands to return turntable to home position. |
| E06 | Set `ManCmd.LeftConveyor` and `ManCmd.RightConveyor` | Which sensors switch when a box reaches each exit | As the box is dispatched, it hits `I_AtLeftEntry` (or `I_AtRightEntry`). At the very end of the line, it clears `I_AtLeftExit` (or `I_AtRightExit`) by dropping from TRUE to FALSE (normally closed behavior). |
| E07 | Switch `ManCmd.RemoverLeft` and `ManCmd.RemoverRight` TRUE and FALSE | Effect on boxes at the end of each exit conveyor | When set to TRUE, the remover instantly despawns/deletes any box touching the end of the conveyor, clearing the exit lines. |
| E08 | Set `DB_Machine.CountTotal` to 5 | Does the operator panel counter show 5? | Yes, the digital display unit on the operator panel updates immediately and shows the integer value 5. |

## Sensor roles (to complete)

| Tag | Role confirmed |
| --- | --- |
| `I_AtBack` | Rear sensor, used to confirm a box has fully entered the entry conveyor area. |
| `I_AtEntry` | Entry detection photocell. Detects the box right at the emitter output before it hits the conveyors. |
| `I_AtFront` | Front queue sensor, detects a box right before it enters the turntable to prevent collisions. |
| `I_AtLeftEntry` | Detects that a box has successfully crossed the gap from the turntable to the Left exit conveyor. |
| `I_AtLeftExit` | Normally Closed (NC) sensor at the end of the left line. Drops to FALSE when a box is about to fall into the remover. |
| `I_AtLoadPosition` | Mechanical limit switch indicating the turntable is in its home position, aligned with the entry line. |
| `I_AtRightEntry` | Detects that a box has successfully crossed the gap from the turntable to the Right exit conveyor. |
| `I_AtRightExit` | Normally Closed (NC) sensor at the end of the right line. Drops to FALSE when a box is about to fall into the remover. |
| `I_AtTurntableEntry` | Central reflective photocell embedded inside the turntable. Used to stop and center the box perfectly on the axis. |
| `I_AtUnloadPosition` | Mechanical limit switch indicating the turntable has fully completed its 90° clockwise rotation. |
