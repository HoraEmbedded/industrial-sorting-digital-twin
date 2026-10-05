# Environment Audit

This document describes the workstation used for the project. It is a reference for compatibility, troubleshooting and reproducibility.

## Workstation

| Item | Value |
| --- | --- |
| Manufacturer | HP |
| Model | HP Envy x360 2-in-1 Laptop 15-fe1xxx |
| CPU | Intel(R) Core(TM) Ultra 7 155U |
| RAM | 32.0 GB |
| Storage | 954 GB |
| GPU | None |
| Operating system | Windows 11 |
| Architecture | 64-bit |

## Software

| Software | Version installed | Role |
| --- | --- | --- |
| TIA Portal | V18 | PLC programming |
| S7-PLCSIM | V18 SP2 | PLC runtime simulation |
| Factory I/O | 2.5.10 Ultimate Edition | Digital twin |
| Factory I/O S7-PLCSIM driver | Bundled with Factory I/O 2.5.10 | Co-simulation link |
| Automation License Manager | V6.2 + SP5 | TIA Portal license management |
| Git for Windows | 2.53.0.windows.1 | Version control |
| VS Code | 1.139.1 | Documentation and scripts editor |
| QElectroTech | 0.90 | Electrical schematic (sheets 1 and 2) |
| Python | 3.13 | Electrical schematic generator (sheets 3 to 5) |

## Compatibility notes

- TIA Portal and S7-PLCSIM must be in the same version. Both are V18 here, with S7-PLCSIM at V18 SP2.
- The Factory I/O S7-PLCSIM driver is installed together with Factory I/O. No separate version is tracked.
- The Automation License Manager must be the latest version available. The installed version is V6.2 + SP5.
- The on-board I/O of the CPU 1214C is moved to start address 100 to avoid overlapping the process image written by Factory I/O.
- Python 3.13 is used only for the electrical schematic generator (`scripts/generate_wiring.py`). It is not part of the PLC runtime chain.

## Verification checklist

Before a work session:

1. Confirm TIA Portal and S7-PLCSIM versions in the TIA Portal About dialog.
2. Confirm Factory I/O version in the Factory I/O About dialog.
3. Confirm the Siemens S7-PLCSIM driver is selected in the Factory I/O Drivers menu.
4. Confirm the Automation License Manager version in its About dialog.
5. Confirm Python 3.13 is on the PATH (`python --version`).

## How to update this file

1. Reopen each tool.
2. Read the exact version in the About dialog.
3. Update the tables above.
4. If a version changed and caused an issue, add an entry to `TROUBLESHOOTING.md`.
5. Commit with a message like `docs: update environment audit`.