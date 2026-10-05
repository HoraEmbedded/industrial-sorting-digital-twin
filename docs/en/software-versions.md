# Software Versions

This document records the reference versions used for the project. Update it whenever a version changes.

## Reference environment

| Software | Version | Role |
| --- | --- | --- |
| Windows | 11 (64-bit) | Host operating system |
| TIA Portal | V18 | PLC programming and project management |
| S7-PLCSIM | V18 SP2 | PLC runtime simulation |
| Factory I/O | 2.5.10 Ultimate Edition | Digital twin and 3D scene |
| Factory I/O S7-PLCSIM driver | Bundled with Factory I/O 2.5.10 | Co-simulation between Factory I/O and S7-PLCSIM |
| Automation License Manager | V6.2 + SP5 | TIA Portal license management |
| Git for Windows | 2.53.0.windows.1 | Version control |
| VS Code | 1.139.1 | Code and documentation editor |
| QElectroTech | 0.90 | Electrical schematic (sheets 1 and 2) |
| Python | 3.13 | Python-generated schematic sheets (3 to 5) |

## Notes

- TIA Portal version must match the S7-PLCSIM version. Both are V18.
- The Factory I/O S7-PLCSIM driver is installed together with Factory I/O. No separate version is tracked.
- The on-board I/O of the CPU 1214C is moved to start address 100 so it never overlaps the process image written by Factory I/O.
- Keep a note of the exact versions in the final report.

## Update procedure

When a version changes:

1. Update the table above.
2. Add an entry to `TROUBLESHOOTING.md` if the change caused any issue.
3. Commit with a message like `chore: update software version table`.