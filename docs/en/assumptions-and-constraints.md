# Assumptions and Constraints

## Technical assumptions

- The PLC is a Siemens S7-1200 CPU 1214C DC/DC/DC or an S7-1500 simulated with PLCSIM
- The simulation runs locally on a single Windows workstation
- TIA Portal is used for programming and for the I/O table
- PLCSIM handles the PLC runtime
- Factory I/O handles the physical scene and the digital twin
- The Factory I/O Siemens S7-PLCSIM driver is used for co-simulation
- All signals between the PLC and the twin are boolean

## Functional assumptions

- Two box sizes are handled: small and large
- Two sorting lanes are available
- One pusher per lane
- Photoelectric sensors detect box presence and size
- An end of lane sensor confirms evacuation

## Constraints

- Windows only for TIA Portal, PLCSIM and Factory I/O
- License availability for TIA Portal and Factory I/O
- Simulation performance limited by the workstation hardware
- No real safety PLC, so the emergency stop is simulated
- English as the primary language for code, documentation and commits
- No em dashes in any file or commit message

## Open questions

- Exact TIA Portal version to be used
- Exact Factory I/O version to be used
- Whether S7-1200 or S7-1500 will be the final target