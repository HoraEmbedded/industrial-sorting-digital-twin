# Software Versions

This document records the reference versions used for the project. Update it whenever a version changes.

## Reference environment

| Software              | Version           | Role                                       |
|-----------------------|-------------------|--------------------------------------------|
| Windows               | 10 or 11 (64-bit) | Host operating system                      |
| TIA Portal            | V16 or later      | PLC programming and project management     |
| S7-PLCSIM             | Matching TIA      | PLC runtime simulation                     |
| Factory I/O           | Latest stable     | Digital twin and 3D scene                  |
| Factory I/O S7 driver | Latest stable     | Co-simulation between Factory I/O and PLCSIM |
| Git for Windows       | Latest stable     | Version control                            |
| VS Code               | Latest stable     | Code and documentation editor              |
| QElectroTech          | Latest stable     | Electrical schematic (or AutoCAD)          |

## Notes

- TIA Portal version must match the PLCSIM version
- The Factory I/O S7 driver must be compatible with the installed PLCSIM version
- Keep a note of the exact versions in the final report

## Update procedure

When a version changes:

1. Update the table above
2. Add an entry to `TROUBLESHOOTING.md` if the change caused any issue
3. Commit with a message like `chore: update software version table`