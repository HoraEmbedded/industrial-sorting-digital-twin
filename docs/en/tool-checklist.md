# Tool Checklist

Checklist to verify that every tool works before starting a work session.

## Before every session

- [ ] Close unused applications to free RAM
- [ ] Plug in the laptop if on battery
- [ ] Confirm that no Windows update is pending
- [ ] Confirm that no TIA Portal background service is stuck (check Task Manager)

## TIA Portal

- [ ] Launch TIA Portal
- [ ] Open the project
- [ ] Verify that the PLC is in `STOP` mode before downloading
- [ ] Compile the project with no errors
- [ ] Confirm the target PLC model matches the one configured

## PLCSIM

- [ ] Launch PLCSIM
- [ ] Confirm the instance matches the PLC model in the project
- [ ] Confirm the PLCSIM instance is in `RUN` before testing
- [ ] Check the CPU LEDs in the PLCSIM window (green means running)

## Factory I/O

- [ ] Launch Factory I/O
- [ ] Open the sorting line scene
- [ ] Verify that the driver `Siemens S7-PLCSIM` is selected in the Drivers menu
- [ ] Confirm the driver is connected (green indicator)
- [ ] Verify the I/O mapping window matches the PLC tag table

## Co-simulation

- [ ] PLCSIM is in `RUN`
- [ ] Factory I/O driver is connected
- [ ] Press Start in Factory I/O and observe the scene
- [ ] Confirm that the PLC outputs drive the actuators

## After every session

- [ ] Put PLCSIM in `STOP`
- [ ] Disconnect the Factory I/O driver
- [ ] Save the Factory I/O scene
- [ ] Save and close the TIA Portal project
- [ ] Commit and push any change to GitHub