# Industrial Sorting Digital Twin

Digital twin and PLC control of an industrial box sorting line, built with Siemens TIA Portal, S7-PLCSIM and Factory I/O.

![Status](https://img.shields.io/badge/status-completed-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![PLC](https://img.shields.io/badge/PLC-Siemens%20S7--1200-blue)
![Twin](https://img.shields.io/badge/twin-Factory%20I%2FO-green)
![Tests](https://img.shields.io/badge/tests-29%20passed-green)

🇬🇧 English (current) | 🇫🇷 [Français](README.fr.md)

## Overview

This project covers the full engineering workflow of an automated sorting line, from requirements to electrical cabinet design, and validates the control program entirely in simulation.

- Functional specification and I/O mapping
- PLC programming in TIA Portal (S7-1200, Ladder)
- Digital twin configuration in Factory I/O
- Co-simulation between S7-PLCSIM and Factory I/O
- Electrical design of the control cabinet
- Embedded performance indicators computed in the PLC
- Documented test plan and final technical report

It is built as a portfolio project for industrial automation and PLC programming roles.

## Key results

| Result | Value |
| --- | --- |
| Validated tests | **29** (13 modes and safety, 12 sorting logic, 4 pipelined emission) |
| Throughput | **144 boxes/hour**, up from 119 with one box at a time (**+21%**) |
| Program structure | **6 code blocks**, 2 data structures |
| Digital twin | Factory I/O scene *Sorting by Height (Advanced)*, 18 inputs and 17 outputs mapped |
| Electrical design | **5 schematic sheets**, 24 V budget of 2.80 A, hardware emergency stop |
| I/O allocation | 14 on-board inputs + 4 on SM 1221 DI 8, 9 on-board outputs + 6 on SM 1222 DQ 8 |

## The simulated line

The digital twin is the Factory I/O scene **Sorting by Height (Advanced)**. Boxes of two heights arrive on an entry conveyor and cross a light curtain that measures them. A turntable then routes each box to the left or right exit conveyor: low boxes to the left, high boxes to the right. An operator panel provides Start, Stop, Reset, Emergency stop, a Manual/Auto selector and a box counter display.

The controller is a Siemens S7-1200 CPU 1214C DC/DC/DC, programmed in Ladder, executed on S7-PLCSIM and linked to the scene through the Siemens S7-PLCSIM driver.

## Technology

| Tool | Version or model | Role |
| --- | --- | --- |
| Siemens TIA Portal | V18 | PLC programming |
| Siemens S7-1200 | CPU 1214C DC/DC/DC, firmware V4.6 | Target controller |
| S7-PLCSIM | V18 SP2 | Virtual PLC |
| Factory I/O | 2.5.10 Ultimate Edition | Digital twin |
| QElectroTech | 0.90 | Electrical schematic, sheets 1 and 2 |
| Python | 3.13 | Electrical schematic generator, sheets 3 to 5 |
| Git and GitHub | - | Version control and CI |

## Repository structure

```
.
├── docs/          Technical documentation (en/, fr/, images/)
├── factory-io/    Scene notes and configuration
├── plc/           Readable PLC exports (XML, PDF printouts)
├── tia-portal/    Archived TIA Portal projects
├── electrical/    Electrical schematic (QElectroTech and generated sheets)
├── kpi/           KPI definitions and results
├── screenshots/   Portfolio screenshots
├── videos/        Demo video and links
├── report/        Final PDF report and LaTeX sources
└── scripts/       Repository checks and Git hooks
```

## Documentation

- English documentation index: [docs/en](docs/en/README.md)
- French documentation index: [docs/fr](docs/fr/README.md)
- Co-simulation runbook: [docs/en/runbook-co-simulation.md](docs/en/runbook-co-simulation.md)
- PLC test log: [docs/en/plc-test-log.md](docs/en/plc-test-log.md)
- Troubleshooting log: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Project status

| Phase | Content | Status |
| --- | --- | --- |
| 1 | Foundation: scope, architecture, environment audit, I/O mapping | Done |
| 2 | PLC safety and modes (`FB_ModeManager`) | Done |
| 3 | Repository structure and bilingual documentation | Done |
| 4 | Sorting logic and pipelined emission (`FB_SortingLogic`) | Done |
| 5 | Co-simulation tests (S7-PLCSIM and Factory I/O) | Done |
| 6 | Electrical schematic (5 sheets) | Done |
| 7 | KPI block (`FB_Kpi`), screenshots and watch tables | Done |
| 8 | Final report and release v1.0 | Done |

## Getting started

1. Clone the repository.
2. Install the tools listed in [docs/en/software-versions.md](docs/en/software-versions.md).
3. Follow the [co-simulation runbook](docs/en/runbook-co-simulation.md) to start TIA Portal, S7-PLCSIM and Factory I/O in the right order.
4. Run the test plan in [docs/en/plc-test-log.md](docs/en/plc-test-log.md) to reproduce the 29 validations.

## Language policy

English is the reference language of this repository. French translations are progressively added in `docs/fr` and in [README.fr.md](README.fr.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the MIT license. See [LICENSE](LICENSE).

## Author

[HoraEmbedded](https://github.com/HoraEmbedded)

