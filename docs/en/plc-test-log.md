# PLC Test Log

This document records the tests performed on the PLC program, with expected and observed results.

## Mission 5 - FB_Mode_Manager tests

### Test 1 - Normal start

- Setup: Emergency_Stop = 1, Stop_Button = 1, Mode_Auto = 1, Start pulsed
- Expected: System_Running = 1, Motor_Main_Conveyor = 1, Light_Green = 1, Light_Red = 0
- Observed: <fill in>

### Test 2 - Stop by Stop button

- Setup: System_Running = 1, Stop_Button set to 0
- Expected: System_Running = 0, Motor_Main_Conveyor = 0, Light_Green = 0, Light_Red = 1
- Observed: <fill in>

### Test 3 - Emergency stop

- Setup: System_Running = 1, Emergency_Stop set to 0
- Expected: System_Running = 0, System_Fault = 1, Motor_Main_Conveyor = 0, Light_Red = 1
- Observed: <fill in>

### Test 4 - Reset after emergency stop

- Setup: System_Fault = 1, Emergency_Stop set back to 1, Start pulsed
- Expected: System_Fault = 0, System_Running = 1
- Observed: <fill in>

## Mission 6 - FB_Sorting_Logic tests

### Test 1 - Small box classification

- Setup: System_Running = 1, Sensor_Size_Low = 1, Sensor_Size_High = 0, Sensor_Entry pulsed
- Expected: Box_Is_Small = 1, Alignment_Done = 1, Pusher_1_Command = 1
- Observed: <fill in>

### Test 2 - Lane 1 evacuation

- Setup: Sensor_Evac_Lane_1 pulsed
- Expected: Pusher_1_Command = 0, Box_Is_Small = 0, Counter_Lane_1 = 1
- Observed: <fill in>

### Test 3 - Large box classification

- Setup: Sensor_Size_Low = 1, Sensor_Size_High = 1, Sensor_Entry pulsed
- Expected: Box_Is_Large = 1, Alignment_Done = 1, Pusher_2_Command = 1
- Observed: <fill in>

### Test 4 - Lane 2 evacuation

- Setup: Sensor_Evac_Lane_2 pulsed
- Expected: Pusher_2_Command = 0, Box_Is_Large = 0, Counter_Lane_2 = 1
- Observed: <fill in>