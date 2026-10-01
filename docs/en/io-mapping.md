# I/O Mapping

Definitive mapping between PLC tags in TIA Portal and Factory I/O signals.

## Reference

- PLC: Siemens S7-1200 CPU 1214C DC/DC/DC
- Simulator: S7-PLCSIM
- Digital twin: Factory I/O, scene Sorting by Height (Advanced)
- Driver: Siemens S7-PLCSIM

## Inputs

| PLC tag                 | Address | Type | Factory I/O signal   | Function                     |
|-------------------------|---------|------|----------------------|------------------------------|
| Start_Button            | %I0.0   | Bool | Start                | Start button, NO             |
| Stop_Button             | %I0.1   | Bool | Stop                 | Stop button, NC              |
| Emergency_Stop          | %I0.2   | Bool | Emergency stop       | Emergency stop, NC           |
| Mode_Auto               | %I0.3   | Bool | Auto                 | Mode selector, 1 for auto    |
| Sensor_Entry            | %I0.4   | Bool | At entry             | Box entry detection          |
| Sensor_Size_Low         | %I0.5   | Bool | Low box              | Small box detection          |
| Sensor_Size_High        | %I0.6   | Bool | High box             | Large box detection          |
| Sensor_Left_Entry       | %I0.7   | Bool | At left entry        | Left lane entry              |
| Sensor_Evac_Lane_1      | %I1.0   | Bool | At left exit         | Left lane evacuation         |
| Sensor_Evac_Lane_2      | %I1.1   | Bool | At right exit        | Right lane evacuation        |
| Reset_Button            | %I1.2   | Bool | Reset                | Reset button, NO             |
| Sensor_Load_Position    | %I1.3   | Bool | At load position     | Load position reached        |
| Sensor_Unload_Position  | %I1.4   | Bool | At unload position   | Unload position reached      |

## Outputs

| PLC tag              | Address | Type | Factory I/O signal | Function                   |
|----------------------|---------|------|---------------------|----------------------------|
| Light_Green          | %Q0.0   | Bool | Green indicator     | Machine running            |
| Light_Red            | %Q0.1   | Bool | Red indicator       | Machine stopped or fault   |
| Motor_Main_Conveyor  | %Q0.2   | Bool | Entry conveyor      | Entry conveyor motor       |
| Motor_Lane_1         | %Q0.3   | Bool | Left conveyor       | Left lane conveyor motor   |
| Motor_Lane_2         | %Q0.4   | Bool | Right conveyor      | Right lane conveyor motor  |
| Pusher_1_Command     | %Q0.5   | Bool | Remover left        | Left remover command       |
| Pusher_2_Command     | %Q0.6   | Bool | Remover right       | Right remover command      |
| Reset_Light          | %Q0.7   | Bool | Reset light         | Fault indicator            |
| Motor_Feeder         | %Q1.0   | Bool | Feeder conveyor     | Feeder conveyor motor      |
| Light_Yellow         | %Q1.1   | Bool | Yellow indicator    | Warning indicator          |
| Turn_Command         | %Q1.2   | Bool | Turn                | Turntable command          |

## Internal memory bits

| PLC tag              | Address | Type | Function                   |
|----------------------|---------|------|----------------------------|
| System_Running       | %M0.0   | Bool | System running state       |
| System_Fault         | %M0.1   | Bool | System fault state         |
| Box_Detected         | %M0.2   | Bool | Box currently detected     |
| Box_Is_Small         | %M0.3   | Bool | Current box is small       |
| Box_Is_Large         | %M0.4   | Bool | Current box is large       |

## Rules

- This file is the single source of truth for the mapping
- Any change must be applied to both TIA Portal and Factory I/O
- Never reuse an address for two different signals
- Factory I/O internal signals (Paused, Running, Reset, Time Scale, Camera Position) are never mapped
- The emitter is controlled by Factory I/O, not by the PLC