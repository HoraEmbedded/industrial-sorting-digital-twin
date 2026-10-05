
# Assumptions and Constraints

## Technical assumptions

- The PLC is a Siemens S7-1200 CPU 1214C DC/DC/DC, simulated with S7-PLCSIM.
- The simulation runs locally on a single Windows workstation.
- TIA Portal V18 is used for programming and for the I/O table.
- S7-PLCSIM handles the PLC runtime.
- Factory I/O 2.5.10 handles the physical scene and the digital twin.
- The Factory I/O Siemens S7-PLCSIM driver is used for co-simulation.
- All signals between the PLC and the twin are Boolean, except the counter display (DInt).
- The on-board I/O of the CPU is moved to start address 100 to avoid overlapping the process image written by Factory I/O.

## Functional assumptions

- Two box types are handled: low box and high box.
- Two exit lanes are available: left for low boxes, right for high boxes.
- The turntable rotates 90 degrees clockwise and returns home when the rotation command is released.
- The light curtain has two beams: the bottom beam detects any box, the top beam detects high boxes only.
- The exit sensors are normally closed: they drop to FALSE when a box reaches the end of the conveyor.
- The emitter is controlled by the PLC through `Q_Emit`: one pulse generates one box.

## Constraints

- Windows only for TIA Portal, S7-PLCSIM and Factory I/O.
- License availability for TIA Portal and Factory I/O.
- Simulation performance limited by the workstation hardware.
- No real safety PLC: the emergency stop is simulated in the program, and the electrical study uses a standard relay. A certified safety relay would be required on a real machine.
- English as the primary language for code, documentation and commits.
- No em dashes in any file or commit message.

## Open questions

- None at this stage. The choice of S7-1200 CPU 1214C DC/DC/DC is final.
- Moving to a real machine would require a risk assessment (ISO 12100) and a certified safety relay (ISO 13849-1).