# Electrical design basis

Theoretical wiring of the control cabinet of the sorting line. The cabinet is not built: this document and the drawings in `electrical/` show how the PLC tags would be wired on real hardware. The QElectroTech source is `electrical/industrial-sorting-line.qet`.

## Scope

In scope: power distribution, motor starters, 24 V DC supply, emergency stop circuit, PLC wiring, operator panel, sensors and indicators.

Not wired, because they only exist in the simulation:

- `Q_Emit`: box emitter of the Factory I/O scene
- `Q_Counter`: counter display of the operator panel (an HMI value on real hardware)
- Factory I/O system tags (Pause, Reset, Run, Time Scale, Camera Position)

## Assumptions

All values are typical and must be replaced by datasheet values for a real build.

- Supply: 400 V three-phase with neutral and PE, 50 Hz. Control supply: 230 V single-phase from L1 and N.
- Motors: three-phase squirrel cage, 0.37 kW, 400 V, about 1.1 A. Motor protection circuit breakers set between 1 and 1.6 A.
- Contactor coils: 24 V DC, about 0.1 A.
- Solenoid valves: 24 V DC, about 0.25 A.
- Indicator lamps: 24 V DC LED, about 0.05 A.
- Sensors: PNP, normally open, three-wire, 24 V DC, about 30 mA each. The light curtain draws about 200 mA and has two PNP outputs.
- The CPU 1214C DC/DC/DC draws about 500 mA on its own (Siemens datasheet).

## Devices

| Designation | Description | Used for |
| --- | --- | --- |
| -Q1 | Main disconnect switch, 3 poles | Incoming 400 V supply |
| -Q2 to -Q6 | Motor protection circuit breakers, 3 poles | Motors M1 to M5 |
| -KM1 to -KM6 | Contactors, 24 V DC coil | Motor starters |
| -M1 | Feeder conveyor motor | `Q_FeederConveyor` |
| -M2 | Entry conveyor motor | `Q_EntryConveyor` |
| -M3 | Left conveyor motor | `Q_LeftConveyor` |
| -M4 | Right conveyor motor | `Q_RightConveyor` |
| -M5 | Turntable roller motor, reversing | `Q_Load` forward (-KM5), `Q_Unload` reverse (-KM6) |
| -YV1 | Solenoid valve of the turntable rotary actuator (spring return) | `Q_Turn` |
| -YV2, -YV3 | Solenoid valves of the end of line removers | `Q_RemoverLeft`, `Q_RemoverRight` |
| -F2 | Circuit breaker 1P+N, 2 A | 230 V control supply |
| -G1 | Power supply 230 V AC to 24 V DC, 5 A | 24 V DC distribution |
| -F3, -F4 | DC circuit breakers, 2 A | Branch +24V (PLC, sensors, lamps), branch of the loads |
| -KA1 | Emergency relay, 24 V DC coil | Cuts the load supply of the CPU outputs |
| -A1 | CPU 1214C DC/DC/DC, 6ES7 214-1AG40-0XB0 | Controller |
| -A2 | SM 1221 DI 8 x 24 V DC, 6ES7 221-1BF32-0XB0 | Extra inputs |
| -A3 | SM 1222 DQ 8 x 24 V DC transistor, 6ES7 222-1BF32-0XB0 | Lamp outputs |
| -S0 | Emergency stop, 2 NC contacts | Hardware cut and PLC input |
| -S1 | Start pushbutton, NO | `I_Start` |
| -S2 | Stop pushbutton, NC | `I_Stop` |
| -S3 | Reset pushbutton, NO | `I_Reset` |
| -S4 | Manual/Auto selector, 2 contacts | `I_Manual`, `I_Auto` |
| -B1 to -B10 | Photoelectric or proximity sensors, PNP NO | See I/O tables |
| -B11 | Light curtain, 2 PNP outputs | `I_LowBox`, `I_HighBox` |
| -H1 to -H3 | Tower lamps green, yellow, red | Machine state |
| -H4 to -H6 | Pushbutton lamps start, stop, reset | Pushbutton feedback |

The article numbers of the signal modules must be confirmed in the TIA Portal hardware catalog.

## Inputs (18)

| Tag | Device | Module and channel | Address on real hardware |
| --- | --- | --- | --- |
| `I_EmergencyStop` | -S0 contact 2 (NC) | -A1 | I0.0 |
| `I_Stop` | -S2 (NC) | -A1 | I0.1 |
| `I_Start` | -S1 (NO) | -A1 | I0.2 |
| `I_Reset` | -S3 (NO) | -A1 | I0.3 |
| `I_Auto` | -S4 contact 1 | -A1 | I0.4 |
| `I_Manual` | -S4 contact 2 | -A1 | I0.5 |
| `I_AtEntry` | -B2 | -A1 | I0.6 |
| `I_AtFront` | -B3 | -A1 | I0.7 |
| `I_AtTurntableEntry` | -B4 | -A1 | I1.0 |
| `I_AtLoadPosition` | -B5 | -A1 | I1.1 |
| `I_AtUnloadPosition` | -B6 | -A1 | I1.2 |
| `I_AtLeftEntry` | -B7 | -A1 | I1.3 |
| `I_AtRightEntry` | -B9 | -A1 | I1.4 |
| `I_AtBack` | -B1 | -A1 | I1.5 |
| `I_AtLeftExit` | -B8 | -A2 channel 0 | Assigned by TIA Portal |
| `I_AtRightExit` | -B10 | -A2 channel 1 | Assigned by TIA Portal |
| `I_HighBox` | -B11 high output | -A2 channel 2 | Assigned by TIA Portal |
| `I_LowBox` | -B11 low output | -A2 channel 3 | Assigned by TIA Portal |

Spare: -A2 channels 4 to 7.

## Outputs (15)

| Tag | Device | Module and channel | Address on real hardware |
| --- | --- | --- | --- |
| `Q_FeederConveyor` | -KM1 coil | -A1 | Q0.0 |
| `Q_EntryConveyor` | -KM2 coil | -A1 | Q0.1 |
| `Q_LeftConveyor` | -KM3 coil | -A1 | Q0.2 |
| `Q_RightConveyor` | -KM4 coil | -A1 | Q0.3 |
| `Q_Load` | -KM5 coil | -A1 | Q0.4 |
| `Q_Unload` | -KM6 coil | -A1 | Q0.5 |
| `Q_Turn` | -YV1 | -A1 | Q0.6 |
| `Q_RemoverLeft` | -YV2 | -A1 | Q0.7 |
| `Q_RemoverRight` | -YV3 | -A1 | Q1.0 |
| `Q_GreenIndicator` | -H1 | -A3 channel 0 | Assigned by TIA Portal |
| `Q_YellowIndicator` | -H2 | -A3 channel 1 | Assigned by TIA Portal |
| `Q_RedIndicator` | -H3 | -A3 channel 2 | Assigned by TIA Portal |
| `Q_StartLight` | -H4 | -A3 channel 3 | Assigned by TIA Portal |
| `Q_StopLight` | -H5 | -A3 channel 4 | Assigned by TIA Portal |
| `Q_ResetLight` | -H6 | -A3 channel 5 | Assigned by TIA Portal |

Spare: -A1 Q1.1, -A3 channels 6 and 7.

In the simulation, the on-board I/O of the CPU is moved to start address 100 and Factory I/O writes to the process image, so the addresses of [io-mapping.md](io-mapping.md) differ from the two tables above. On real hardware, the tag table addresses would be changed to match them.

## 24 V DC budget

| Load | Quantity | Current each (A) | Total (A) |
| --- | --- | --- | --- |
| CPU 1214C | 1 | 0.50 | 0.50 |
| Signal modules | 2 | 0.05 | 0.10 |
| Sensors | 10 | 0.03 | 0.30 |
| Light curtain | 1 | 0.20 | 0.20 |
| Indicator lamps | 6 | 0.05 | 0.30 |
| Solenoid valves | 3 | 0.25 | 0.75 |
| Contactor coils | 6 | 0.10 | 0.60 |
| Emergency relay coil | 1 | 0.05 | 0.05 |
| **Total** | | | **2.80** |

With a 30 % margin the need is 3.64 A, so a 24 V DC / 5 A power supply is selected. Branch -F3 (PLC, modules, sensors, lamps) carries about 1.4 A and branch -F4 (valves, coils, relay) about 1.4 A, so both use 2 A breakers.

## Safety concept

- The emergency stop -S0 has two NC contacts. Contact 1 feeds the coil of -KA1. A NO contact of -KA1 supplies the load power of the CPU outputs (rail +24VS), so every actuator drops immediately and in hardware. Contact 2 goes to the PLC input `I_EmergencyStop`.
- The lamp outputs are on -A3, supplied from +24V (not switched), so the red and yellow lamps remain available after an emergency stop.
- -KA1 re-energizes as soon as the button is released. Restart is prevented by the fault latch of `FB_ModeManager` (Reset, then Start).
- This is a portfolio design. A real machine would use a certified safety relay and a safety analysis.
- The coils of -KM5 and -KM6 are interlocked electrically by NC auxiliary contacts.

## Conventions

- Rails and conductors are labelled with their name: L1, L2, L3, N, PE, +24V, +24VS, 0V.
- I/O wires carry the PLC tag name, and the PLC terminals carry the channel address.
- Device labels follow the table above.
- PLC terminal names are copied from the Siemens S7-1200 System Manual.

## Drawing list

| Sheet | Title | Source |
| --- | --- | --- |
| 1 | Main supply and motor starters M1 to M4 | QElectroTech |
| 2 | Turntable roller motor M5 (reversing) | QElectroTech |
| 3 | Control supply 24 V DC and emergency stop | Python generator |
| 4 | PLC inputs | Python generator |
| 5 | PLC outputs | Python generator |

The device list is the Devices table of this document.

## How the drawings are produced

- Sheets 1 and 2 are drawn in QElectroTech (`electrical/industrial-sorting-line.qet`, exported to `electrical/motor-power.pdf`).
- Sheets 3 to 5 are generated by `scripts/generate_wiring.py` from the I/O tables of this document, so the drawings and the tables stay consistent. Run `python scripts/generate_wiring.py`, then print `electrical/wiring-sheets.html` to PDF (`electrical/plc-wiring.pdf`).
- The generated sheets use simplified symbols: sensors, lamps and coils are boxes. Sensors are PNP three-wire devices and only the +24V and signal wires are drawn. Spare channels are not drawn.