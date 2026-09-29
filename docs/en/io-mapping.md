# I/O Mapping

Definitive mapping between the PLC tags in TIA Portal and the Factory I/O signals.

## Reference

- PLC: Siemens S7-1200 CPU 1214C DC/DC/DC
- Simulator: S7-PLCSIM
- Digital twin: Factory I/O
- Driver: Siemens S7-PLCSIM

## Inputs

| PLC tag              | Address | Type | Factory I/O signal           | Function                       |
|----------------------|---------|------|------------------------------|--------------------------------|
| Start_Button         | %I0.0   | Bool | Start push button            | Start command, NO              |
| Stop_Button          | %I0.1   | Bool | Stop push button             | Stop command, NC               |
| Emergency_Stop       | %I0.2   | Bool | Emergency stop               | Emergency stop, NC             |
| Mode_Auto            | %I0.3   | Bool | Mode selector                | 1 for auto, 0 for manual       |
| Sensor_Entry         | %I0.4   | Bool | Entry sensor                 | Box presence detection         |
| Sensor_Size_Low      | %I0.5   | Bool | Low size sensor              | Detects small boxes            |
| Sensor_Size_High     | %I0.6   | Bool | High size sensor             | Detects large boxes            |
| Pusher_1_Retracted   | %I0.7   | Bool | Pusher 1 retracted sensor    | Retracted limit switch         |
| Sensor_Evac_Lane_1   | %I1.0   | Bool | Lane 1 evacuation sensor     | Lane 1 evacuation detection    |
| Sensor_Evac_Lane_2   | %I1.1   | Bool | Lane 2 evacuation sensor     | Lane 2 evacuation detection    |

## Outputs

| PLC tag              | Address | Type | Factory I/O signal           | Function                       |
|----------------------|---------|------|------------------------------|--------------------------------|
| Light_Green          | %Q0.0   | Bool | Green light                  | Machine running                |
| Light_Red            | %Q0.1   | Bool | Red light                    | Machine stopped or fault       |
| Motor_Main_Conveyor  | %Q0.2   | Bool | Main conveyor motor          | Main conveyor drive            |
| Motor_Lane_1         | %Q0.3   | Bool | Lane 1 conveyor motor        | Lane 1 conveyor drive          |
| Motor_Lane_2         | %Q0.4   | Bool | Lane 2 conveyor motor        | Lane 2 conveyor drive          |
| Pusher_1_Command     | %Q0.5   | Bool | Pusher 1                     | Pusher 1 activation            |
| Pusher_2_Command     | %Q0.6   | Bool | Pusher 2                     | Pusher 2 activation            |

## Internal memory bits

| PLC tag              | Address | Type | Function                       |
|----------------------|---------|------|--------------------------------|
| System_Running       | %M0.0   | Bool | System running state           |
| System_Fault         | %M0.1   | Bool | System fault state             |
| Box_Detected         | %M0.2   | Bool | Box currently detected         |
| Box_Is_Small         | %M0.3   | Bool | Current box is small           |
| Box_Is_Large         | %M0.4   | Bool | Current box is large           |

## Rules

- This file is the single source of truth for the mapping
- Any change to an address must be reflected both in TIA Portal and Factory I/O
- Never change an address without updating this file and committing
- Never reuse an address for two different signals