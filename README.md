# Industrial Sorting Digital Twin

Digital twin and PLC control of an industrial sorting line, built with Siemens TIA Portal, S7-PLCSIM and Factory I/O.

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![PLC](https://img.shields.io/badge/PLC-Siemens%20S7--1200-blue)
![Twin](https://img.shields.io/badge/twin-Factory%20I%2FO-green)

🇬🇧 English (current) | 🇫🇷 [Français](README.fr.md)

## Overview

This project covers the full engineering workflow of an automated sorting line:

- Functional specification and I/O mapping
- PLC programming in TIA Portal (S7-1200, ladder logic)
- Digital twin configuration in Factory I/O
- Co-simulation between S7-PLCSIM and Factory I/O
- Electrical schematic
- KPI definition and performance tracking
- Demo video and final technical report

It is built as a portfolio project for industrial automation and PLC programming roles.

## The simulated line

The digital twin is the Factory I/O scene **Sorting by Height (Advanced)**. Boxes of two different heights arrive on an entry conveyor and are measured by a light curtain. A turntable then routes each box to the left or the right exit conveyor. An operator panel provides Start, Stop, Reset, Emergency stop, a Manual/Auto selector and a box counter.

## Technology

| Tool | Version or model | Role |
| --- | --- | --- |
| Siemens TIA Portal | V18 | PLC programming |
| Siemens S7-1200 | CPU 1214C DC/DC/DC, firmware V4.6 | Target controller |
| S7-PLCSIM | Same generation as TIA Portal | Virtual PLC |
| Factory I/O | v2.5.10, Ultimate Edition | Digital twin |
| QElectroTech | - | Electrical schematic |
| Git and GitHub | - | Version control |

## Repository structure

```
.
├── docs/          Technical documentation (en/, fr/, images/)
├── factory-io/    Scene notes and configuration
├── plc/           Readable PLC exports (XML, PDF printouts)
├── tia-portal/    Archived TIA Portal projects
├── electrical/    Electrical schematic (QElectroTech)
├── kpi/           KPI definitions and results
├── screenshots/   Portfolio screenshots
├── videos/        Demo video and links
├── report/        Final PDF report and assets
└── scripts/       Repository checks and Git hooks
```

## Documentation

- English documentation index: [docs/en](docs/en/README.md)
- French documentation index: [docs/fr](docs/fr/README.md)
- Troubleshooting log: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Project status

| Phase | Content | Status |
| --- | --- | --- |
| 1 | Foundation: scope, architecture, environment audit, I/O mapping | Done |
| 2 | PLC safety and modes (`FB_ModeManager`) | Done |
| 3 | Repository cleanup and bilingual documentation | done |
| 4 | Sorting logic for the Advanced scene | Done |
| 5 | Co-simulation tests (S7-PLCSIM and Factory I/O) | Done|
| 6 | Electrical schematic | Done |
| 7 | KPI, demo video and screenshots | Done(KPIs in perspective) |
| 8 | Final report and release v1.0 | Done |

## Getting started

1. Clone the repository.
2. Follow the [co-simulation runbook](docs/en/runbook-co-simulation.md) to start TIA Portal, S7-PLCSIM and Factory I/O in the right order.
3. Full reproduction steps will be published with release v1.0.

## Language policy

English is the reference language. French translations are added progressively in `docs/fr` and in [README.fr.md](README.fr.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the MIT license. See [LICENSE](LICENSE).

## Author

[HoraEmbedded](https://github.com/HoraEmbedded)
