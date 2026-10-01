# TIA Portal project archives

This folder holds archived TIA Portal projects so the work can be restored on another machine.

## Layout

- `exports/`: project archives (`.zap` files) and other exports

## Rules

- Never commit the raw project folder. Archive it from TIA Portal first (Project, Archive).
- Name archives with the date and the milestone, for example `PLC_Sorting_2026-10-15_sorting-logic.zap18`.
- Readable exports of the program (XML, PDF printouts) go to [plc/](../plc/README.md), not here.