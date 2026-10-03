# PLC sources

Readable exports of the PLC program, so the logic can be reviewed on GitHub without opening TIA Portal.

## Layout

- `src/`: block and tag table exports (SimaticML XML)
- `printouts/`: PDF printouts of the program (added when the program is stable)

The archived TIA Portal project itself lives in [tia-portal/](../tia-portal/README.md).

## Program structure

| Block | Role |
| --- | --- |
| OB1 `Main` | Cyclic entry point, calls the blocks below in order |
| FC9000 `MHJ-PLC-Lab-Function-S71200` | Communication function supplied with the Factory I/O template for S7-PLCSIM. Required, must stay first. |
| FB1 `FB_ModeManager` | Auto and Manual selection, Start, Stop, emergency stop fault latch |
| FB2 `FB_SortingLogic` | Sorting sequence, one box at a time (see [docs/en/sorting-sequence.md](../docs/en/sorting-sequence.md)) |
| FC1 `FC_Outputs` | Safety gating and writing of all outputs |
| DB `DB_Machine` | Machine status, actuator commands, counters |

Details and naming conventions: [docs/en/plc-architecture.md](../docs/en/plc-architecture.md).