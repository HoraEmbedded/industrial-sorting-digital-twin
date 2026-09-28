# PLC Program Architecture

This document describes the block structure of the PLC program, the responsibility of each block, and the conventions used throughout the project.

## Design principles

- One block, one responsibility
- No duplicated logic
- All I/O accesses go through named tags
- All blocks are documented with a header comment
- The main cycle stays short and only calls other blocks

## Block structure

### OB1 - Main

- Type: Organization Block
- Language: LAD
- Responsibility: main cycle, calls all other blocks in order
- Called by: the PLC operating system at every scan cycle

### FB1 - FB_Mode_Manager

- Type: Function Block
- Language: LAD
- Instance DB: DB_Mode_Manager
- Responsibility: safety, start and stop, emergency stop, auto and manual mode handling
- Called by: OB1

### FB2 - FB_Sorting_Logic

- Type: Function Block
- Language: LAD or GRAPH
- Instance DB: DB_Sorting_Logic
- Responsibility: box detection, size classification, pusher activation, counters
- Called by: OB1

### FC1 - FC_IO_Mapping

- Type: Function
- Language: LAD or SCL
- Responsibility: mapping between Factory I/O signals and PLC tags, signal conditioning
- Called by: OB1

### DB_Global

- Type: Global Data Block
- Responsibility: global setpoints, counters, configuration values shared between blocks

## Call order in OB1

1. FC_IO_Mapping
2. FB_Mode_Manager
3. FB_Sorting_Logic

The order matters. Mode management must run before sorting logic, so that safety and start conditions are known before the sorting sequence evaluates.

## Naming conventions

### Tags

- PascalCase
- English only
- Prefix by type where useful:
  - `Start_Button`, `Stop_Button`, `Emergency_Stop`
  - `Sensor_Entry`, `Sensor_Size_High`, `Sensor_Size_Low`
  - `Motor_Main_Conveyor`, `Motor_Lane_1`, `Motor_Lane_2`
  - `Pusher_1_Command`, `Pusher_2_Command`
  - `Counter_Lane_1`, `Counter_Lane_2`
- Boolean tags do not start with "b" or "is"
- Avoid abbreviations except common industrial ones

### Blocks

- OB: `Main`
- FB: `FB_<Responsibility>`
- FC: `FC_<Responsibility>`
- Global DB: `DB_<Responsibility>`
- Instance DB: `DB_<FB_Name>`

### Comments

- English only
- Each block starts with a header comment: purpose, inputs, outputs, author, date
- Each network in LAD has a one line comment

## Status

Draft. To be updated if the architecture changes.