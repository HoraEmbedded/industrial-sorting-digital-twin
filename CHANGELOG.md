# Changelog

All notable changes to this project are documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

## [Unreleased]

### Added

- Initial repository structure
- Main README in English
- French README
- MIT license
- Contributing guidelines
- Changelog
- `kpi/` folder with README and data placeholder
- Language switcher between English and French READMEs
- Direct license link in READMEs
- `TROUBLESHOOTING.md` with template and first entry
- Scope definition
- Technical assumptions and constraints
- Software versions reference
- High level architecture diagram
- Milestone plan
- Risk register
- Workstation environment audit
- Tool startup and shutdown checklist
- Real software versions recorded
- PLC program architecture document
- Block structure in TIA Portal: OB1, FB_ModeManager, FB_SortingLogic, FC_Outputs, DB_Global
- Full PLC tag table with symbolic names
- Definitive I/O mapping between TIA Portal and Factory I/O
- Naming conventions for tags, blocks and comments
- FB_ModeManager implementation with safety, mode and start stop logic
- Emergency stop with fault latching, cleared by the Reset button
- Run stop latch with self holding circuit
- Main conveyor motor command
- Indicator lights logic
- PLC test log with four functional tests
- FB_SortingLogic implementation with detection, classification, pushers and counters
- Rising edge detection on entry and evacuation sensors
- SR latches for box classification and pusher commands
- Alignment timer with configurable preset
- Lane counters using ADD_I on rising edge
- PLC test log extended with four sorting tests
- Factory I/O Advanced scene configuration
- Complete I/O mapping for the Advanced scene
- Tag additions: Reset_Button, Reset_Light, Motor_Feeder, Light_Yellow, Turn_Command, Sensor_Left_Entry, Sensor_Load_Position, Sensor_Unload_Position
- Scene behavior document, PLC architecture and naming conventions document
- PDF printout of the rewritten PLC program
- Sorting sequence documentation with Grafcet (`docs/en/sorting-sequence.md`)
- Sorting logic tests T14 to T25 and throughput measurement in the PLC test log
- Scene experiments E09 to E11 (sensor idle levels, exit sensor polarity, emitter settings)
- Screenshots of the sorting logic networks
- Pipelined emission tests T26 to T29 and throughput comparison in the sorting sequence document
- Boxes-in-transit counters per exit conveyor

### Changed

- Split documentation into `docs/en/` and `docs/fr/`
- Updated README with badges, technologies list and language switcher
- Extended gitignore with AutoCAD and QElectroTech rules
- Software versions table updated with installed versions
- `docs/en/io-mapping.md` promoted to single source of truth for the mapping
- Switched from Basic scene to Advanced scene
- Emitter controlled by Factory I/O, not by the PLC
- Turntable command driven by the PLC
- Merged duplicate folders: `report`/`reports`, `video`/`videos`, `schemas`/`electrical`
- Renamed `screenshots/schemas` to `screenshots/electrical`
- Rewrote `README.md` and `README.fr.md` (Advanced scene, roadmap, accents, author name)
- Rewrote the PLC program from scratch for the Advanced scene: tags mirror the Factory I/O names, new `FB_ModeManager`, `FC_Outputs`, `DB_Machine` and `UDT_ActuatorCmd`
- Renamed `FB_Mode_Manager`, `FB_Sorting_Logic` and `FC_IO_Mapping` to `FB_ModeManager`, `FB_SortingLogic` and `FC_Outputs`
- Moved the on-board DI/DQ addresses of the CPU to 100 to avoid overlap with Factory I/O
- Stop now requests a stop at the end of the cycle, as in the functional specification
- Rewrote the I/O mapping, PLC architecture and PLC test log documents
- Implemented `FB_SortingLogic`: Grafcet with 7 steps, height classification, turntable control, exit counting, stop at the end of the cycle
- Extended `DB_Machine` with `SortStep`, `ClearCounters` and `ExitIdleHigh`
- OB1 passes sensors and counters to `FB_SortingLogic`. Reset in Manual mode zeroes the counters
- Project status in the READMEs: cleanup, sorting logic and co-simulation tests marked as done
- The next box is emitted as soon as the previous one leaves the turntable (step 5 goes directly to step 1, step 6 removed)
- Feeder and entry conveyors wait when a box is in front of a turntable that is not at home
- Height and entry latches are cleared at step 1
- Centering delay documented (`CenterTime`)
- Harmonized sensor tag names (`I_At...`) between TIA Portal and the documentation

### Removed

- Stray `test.md` file
- Old blocks `FB_Mode_Manager`, `FB_Sorting_Logic`, `FC_IO_Mapping`, `DB_Global` and the old default tag table content