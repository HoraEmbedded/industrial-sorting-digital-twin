# PLC sources

Readable exports of the PLC program, so the logic can be reviewed on GitHub without opening TIA Portal.

## Layout

- `src/`: block and tag table exports (SimaticML XML)
- `printouts/`: PDF printouts of the program (added when the program is stable)

The archived TIA Portal project itself lives in [tia-portal/](../tia-portal/README.md).

## Program structure

| Block | Role |
| --- | --- |
| OB1 `Main` | Cyclic entry point, calls the blocks below |
| FB1 `FB_Mode_Manager` | Safety, run and stop latch, indicator lights |
| FB2 `FB_Sorting_Logic` | Sorting sequence |
| FC1 `FC_IO_Mapping` | Output mapping |
| FC9000 `MHJ-PLC-Lab-Function-S71200` | Communication function supplied with the Factory I/O template for S7-PLCSIM. Required to link the simulator to Factory I/O. Do not remove. |

Details and naming conventions: [docs/en/plc-architecture.md](../docs/en/plc-architecture.md).