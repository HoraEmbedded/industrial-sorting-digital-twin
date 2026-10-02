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
