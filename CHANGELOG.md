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
- Block structure in TIA Portal: OB1, FB_Mode_Manager, FB_Sorting_Logic, FC_IO_Mapping, DB_Global
- Full PLC tag table with symbolic names
- Definitive I/O mapping between TIA Portal and Factory I/O
- Naming conventions for tags, blocks and comments
- FB_Mode_Manager implementation with safety, mode and start stop logic
- Emergency stop with fault latching on rising edge of Start
- Run stop latch with self holding circuit
- Main conveyor motor command
- Indicator lights logic
- PLC test log with four functional tests
- FB_Sorting_Logic implementation with detection, classification, pushers and counters
- Rising edge detection on entry and evacuation sensors
- SR latches for box classification and pusher commands
- Alignment timer with configurable preset
- Lane counters using ADD_I on rising edge
- PLC test log extended with four sorting tests
- Factory I/O Advanced scene configuration
- Complete I/O mapping for the Advanced scene
- Tag additions: Reset_Button, Reset_Light, Motor_Feeder, Light_Yellow, Turn_Command, Sensor_Left_Entry, Sensor_Load_Position, Sensor_Unload_Position

### Changed

- Split documentation into `docs/en/` and `docs/fr/`
- Updated README with badges, technologies list and language switcher
- Extended gitignore with AutoCAD and QElectroTech rules
- Software versions table updated with installed versions
- `docs/en/io-mapping.md` promoted to single source of truth for the mapping
- Switched from Basic scene to Advanced scene
- Emitter controlled by Factory I/O, not by the PLC
- Turntable command driven by the PLC

