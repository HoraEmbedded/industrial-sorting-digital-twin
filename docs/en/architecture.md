# Architecture

This document describes the software architecture of the PLC program and the digital twin. Detailed information is in [plc-architecture.md](plc-architecture.md) and [io-mapping.md](io-mapping.md).

## PLC program structure (TIA Portal)

- `OB1` Main: main cycle, calls the blocks below in order.
- `FC9000`: link with S7-PLCSIM, supplied with the Factory I/O template, always called first.
- `FB_ModeManager`: Auto and Manual selection, Start, Stop, emergency stop fault latch.
- `FB_SortingLogic`: sorting sequence, box emission, counting, pipelined emission.
- `FC_Outputs`: single writer of all outputs, with safety gating, lamps and counter display.
- `FB_Kpi`: availability, throughput and average cycle time computed in the PLC.
- `DB_Machine`: machine state, actuator commands, counters.
- `UDT_ActuatorCmd`: one command bit per actuator.

## Digital twin (Factory I/O)

- Scene: Sorting by Height (Advanced), Factory I/O 2.5.10 Ultimate Edition.
- Light curtain for box height measurement, turntable with rollers for routing.
- Left and right exit conveyors, end of line removers.
- Operator panel with Start, Stop, Reset, emergency stop, Auto/Manual selector and counter display.
- Co-simulation with S7-PLCSIM through the Siemens S7-PLCSIM driver.

## Data flow

1. Inputs feed `FB_ModeManager` and `FB_SortingLogic`.
2. Both exchange data with `DB_Machine`.
3. `FC_Outputs` reads `DB_Machine` and the emergency stop input, then writes all `Q_` outputs.
4. `FB_Kpi` reads the machine state and updates the KPI variables in `DB_Machine`.

## Status

Completed. See [sorting-sequence.md](sorting-sequence.md) for the sequence and [electrical-design.md](electrical-design.md) for the cabinet.