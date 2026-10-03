# PLC test log

Tests run with S7-PLCSIM and Factory I/O. Results: Pass, Fail or Not run.



## Foundation tests (modes and safety)

| ID | Condition | Action | Expected | Result | Date |
| --- | --- | --- | --- | --- | --- |
| T01 | Scene started, selector in Manual | None | `I_Stop`, `I_EmergencyStop`, `I_Manual` TRUE. `ManualMode` TRUE, `Run` FALSE. Red and yellow lamps on. | Pass | 2026-10-02 |
| T02 | After T01 | Selector to Auto | `AutoMode` TRUE, `ManualMode` FALSE. Yellow off, red on. | Pass | 2026-10-02 |
| T03 | Auto, stopped | Press Start | `Run` TRUE. Green and start light on, red and stop light off. | Pass | 2026-10-02 |
| T04 | Running | Press Stop | `Run` FALSE (the placeholder sorting logic reports idle). Red on. | Pass | 2026-10-02 |
| T05 | Running | Press Emergency stop | `Fault` TRUE, `Run` FALSE. Yellow on, reset light off. | Pass | 2026-10-02 |
| T06 | After T05 | Release Emergency stop | `Fault` stays TRUE. Reset light on. | Pass | 2026-10-02 |
| T07 | After T06 | Press Start | Nothing happens, `Run` stays FALSE. | Pass | 2026-10-02 |
| T08 | After T06 | Press Reset | `Fault` FALSE, reset light off, `Run` FALSE. | Pass | 2026-10-02 |
| T09 | After T08, Auto | Press Start | `Run` TRUE. | Pass | 2026-10-02 |
| T10 | Running | Selector to Manual | `Run` FALSE, `ManualMode` TRUE. | Pass | 2026-10-02 |
| T11 | Manual | Set `ManCmd.EntryConveyor` TRUE | `Q_EntryConveyor` TRUE, the entry conveyor moves. | Pass | 2026-10-02 |
| T12 | After T11 | Press Emergency stop | `Q_EntryConveyor` FALSE immediately. | Pass | 2026-10-02 |
| T13 | After T12 | Set `ManCmd.EntryConveyor` FALSE, release Emergency stop, Reset | The conveyor stays stopped. | Pass | 2026-10-02 |
## Sorting logic tests

Run in Auto mode with `WT_Sorting` online, unless stated otherwise.

| ID | Condition | Action | Expected | Result | Date |
| --- | --- | --- | --- | --- | --- |
| T14 | Auto, line empty, table home | Press Start | `SortStep` goes 1, 2, 3, 4, 5, 6, 0. A box is emitted and reaches the turntable. | Pass | 2026-10-03 |
| T15 | During a cycle with a Low box | Observe `WT_Sorting` | `Q_Unload` and `Q_LeftConveyor` TRUE in step 4. The box goes to the left. `CountLeft` increments, `CountRight` does not. | Pass | 2026-10-03 |
| T16 | During a cycle with a High box | Observe `WT_Sorting` | `Q_Load` TRUE in step 4. The box goes to the right. `CountRight` increments, `CountLeft` does not. | Pass | 2026-10-03 |
| T17 | Auto, counters at 0 | Let 10 boxes complete without any intervention | `CountTotal` = `CountLeft` + `CountRight` = 10. No box stuck. The panel counter shows 10. | Pass | 2026-10-03 |
| T18 | A box is on the turntable | Press Stop | The cycle finishes, the box is counted, then `Run` FALSE. No new box is emitted. Red light on. | Pass | 2026-10-03 |
| T19 | A box is on the entry conveyor (step 2) | Press Stop | The box still reaches the exit and is counted before `Run` drops. | Pass | 2026-10-03 |
| T20 | After T18 | Press Start | Emission resumes. Counters keep their values. | Pass | 2026-10-03 |
| T21 | Step 3 (table rotating) | Press Emergency stop | Every `Q_` output FALSE immediately. `Fault` TRUE. After release and Reset: `SortStep` is 0, `Run` FALSE. | Pass | 2026-10-03 |
| T22 | After T21, box still on the turntable | Press Start | `Run` TRUE, `SortStep` stays 0, no box is emitted. | Pass | 2026-10-03 |
| T23 | After T22 | Switch to Manual, clear the box with `ManCmd`, switch to Auto, press Start | Normal cycles resume. | Pass | 2026-10-03 |
| T24 | Mid-cycle | Switch the selector from Auto to Manual | `Run` FALSE, `SortStep` 0, all automatic commands FALSE. | Pass | 2026-10-03 |
| T25 | Manual mode, counters not zero | Press Reset | `CountLeft`, `CountRight` and `CountTotal` are 0, and the panel counter shows 0. | Pass | 2026-10-03 |

## Measurements

| Measurement | Value |
| --- | --- |
| Time for 10 boxes in T17 (s) | 313.0 |
| Throughput (boxes per hour) = 36000 / time | 115.0 |
| Low boxes and High boxes seen in T17 | 6 Low / 4 High |

