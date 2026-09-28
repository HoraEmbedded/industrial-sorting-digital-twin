
# Industrial Sorting Digital Twin

Digital twin and PLC control of an industrial sorting line using TIA Portal, PLCSIM and Factory I/O.

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![PLC](https://img.shields.io/badge/PLC-Siemens%20S7--1200-blue)
![Twin](https://img.shields.io/badge/twin-Factory%20I%2FO-green)

> 🇬🇧 Read this page in English (current)
> 🇫🇷 [Lire cette page en francais](README.fr.md)

## Overview

This project implements the design, programming and simulation of an automated industrial sorting line. It covers the full engineering workflow:

- Functional specifications and I/O mapping
- PLC programming in TIA Portal (S7-1200 / S7-1500, LAD and GRAPH)
- Digital twin configuration in Factory I/O
- Co-simulation between PLCSIM and Factory I/O
- Electrical schematic
- KPI definition and performance tracking
- Final technical report and demo video

The project is built as a professional portfolio piece for industrial automation, PLC programming and digital twin engineering roles.

## Technologies

- Siemens TIA Portal V1X
- S7-PLCSIM
- Factory I/O
- AutoCAD / QElectroTech
- Git & GitHub

## Repository structure

```text
.
├── docs/              Technical documentation (en / fr)
├── tia-portal/        TIA Portal project exports and sources
├── factory-io/        Factory I/O scenes and configuration
├── plc/               PLC source code (SCL, LAD, GRAPH exports)
├── schemas/           Electrical schematics
├── kpi/               KPI definitions and results
├── screenshots/       Screenshots of the project
├── videos/            Demo videos and links
├── report/            Final PDF report and assets
└── scripts/           Utility scripts
```

## Documentation

- English: [docs/en](docs/en)
- French: [docs/fr](docs/fr) (available at the end of the project)

## Status

In progress. See [CHANGELOG.md](CHANGELOG.md) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE](LICENSE).

## Author

Horaemebedded