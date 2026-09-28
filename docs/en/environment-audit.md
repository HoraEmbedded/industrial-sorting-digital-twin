# Environment Audit

This document describes the workstation used for the project. It is a reference for compatibility, troubleshooting and reproducibility.

## Workstation

## Workstation

| Item              | Value                |
|-------------------|----------------------|
| Manufacturer      | HP         |
| Model             | HP Envy x360 2-in-1 Laptop 15-fe1xxx         |
| CPU               | Intel(R) Core(TM) Ultra 7 155U         |
| RAM               | 32.0 GB         |
| Storage           | 954 GB         |
| GPU               | None         |
| Operating system  | Windows 11    |
| Architecture      | 64-bit               |

## Software

| Software                       | Version installed     |
|--------------------------------|-----------------------|
| TIA Portal                     | V18         |
| S7-PLCSIM                      | V18 SP2         |
| Factory I/O                    | 2.5.10          |
| Factory I/O S7-PLCSIM driver   | <your value>          |
| Automation License Manager     | V6.2 + SP5          |
| Git for Windows                |  2.53.0.windows.1          |
| VS Code                        | 1.139.1          |


## Compatibility notes

- TIA Portal and PLCSIM must be in the same version
- The Factory I/O S7 driver must support the installed PLCSIM version
- The Automation License Manager must be the latest version available

## How to update this file

1. Reopen each tool
2. Read the exact version in the About dialog
3. Update the tables above
4. Commit with a message like `docs: update environment audit`