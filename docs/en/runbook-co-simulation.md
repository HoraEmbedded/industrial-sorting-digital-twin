# Runbook - Co-simulation startup

This runbook describes the exact order of operations to start the co-simulation between TIA Portal, PLCSIM and Factory I/O. Follow it strictly.

## Prerequisites

- TIA Portal, PLCSIM and Factory I/O installed
- Factory I/O S7-PLCSIM driver installed
- No other PLCSIM instance running
- Project compiled without errors

## Startup sequence

1. Close any previous PLCSIM instance
   - Check the Windows Task Manager for leftover S7-PLCSIM processes
   - Kill them if needed

2. Open TIA Portal
   - Open the sorting line project
   - Compile the project with Ctrl+B
   - Confirm zero errors

3. Start PLCSIM from TIA Portal
   - Click the Start simulation button
   - Wait for PLCSIM to open
   - Download the program to the simulated PLC
   - Put the CPU in RUN
   - Confirm the green RUN LED in PLCSIM

4. Open Factory I/O
   - Open the sorting line scene
   - Open the Drivers menu
   - Select Siemens S7-PLCSIM
   - Click CONNECT
   - Confirm the green indicator

5. Test the co-simulation
   - Press Start in Factory I/O
   - Observe the scene
   - Confirm that the PLC outputs drive the actuators
   - Confirm that the sensors feed back into the PLC inputs

## Shutdown sequence

1. Press Stop in Factory I/O
2. Disconnect the driver in Factory I/O
3. Save the Factory I/O scene
4. Put the PLC in STOP in PLCSIM
5. Close PLCSIM
6. Save and close the TIA Portal project

## Troubleshooting quick reference

| Symptom                                       | Likely cause                          | Action                                                 |
|-----------------------------------------------|---------------------------------------|--------------------------------------------------------|
| Driver reports multiple PLCSIM instances      | Several PLCSIM processes running      | Kill extra processes in Task Manager                   |
| Driver connects but no I/O responds           | Wrong I/O mapping                     | Check `docs/en/io-mapping.md`                          |
| PLC refuses to download                       | Compile errors or version mismatch    | Recompile and check TIA Portal and PLCSIM versions     |
| Factory I/O freezes on connect                | PLCSIM not in RUN                     | Put the CPU in RUN before connecting                   |