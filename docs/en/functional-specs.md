# Functional Specifications

## Modes

- Manual mode: `Run` is always FALSE, actuators follow the manual commands for commissioning.
- Automatic mode: `Start` launches production if no fault is present.

## Automatic mode

- Press Start to run the conveyors and start the sorting sequence.
- Press Stop to stop the system at the end of the cycle: no new box is emitted, the box in progress is finished and counted, then the machine stops.
- The emergency stop cuts all actuator outputs immediately, whatever the mode.
- After the emergency stop is released, Reset clears the fault, then Start is required to run again.

## Sorting logic

- The emitter pulse generates one box per cycle (500 ms pulse in step 1).
- The box crosses the light curtain: a low box triggers only the low beam, a high box triggers both beams.
- The program only needs the `I_HighBox` signal: it is latched while the box travels to the turntable.
- Low boxes are routed to the left exit conveyor with the `Unload` roller command.
- High boxes are routed to the right exit conveyor with the `Load` roller command.
- A box is counted on the rising edge of the end sensor of its lane.
- The next box is emitted as soon as the previous one has left the turntable (pipelined emission).

## Signals and polarity

- Start, Reset: normally open (FALSE at rest).
- Stop, emergency stop: normally closed (TRUE at rest, FALSE when pressed or broken).
- Auto / Manual selector: one contact each, one of them TRUE at any time.
- Exit sensors: normally closed, they drop to FALSE when a box reaches the end.

## Outputs and signalling

- Green lamp and Start lamp follow `Run`.
- Red lamp and Stop lamp follow `NOT Run`.
- Yellow lamp is on when `Fault` or `ManualMode`.
- Reset lamp is on when `Fault` is latched and the emergency stop is released.
- The counter display shows `CountTotal`.

## Status

Completed. See [sorting-sequence.md](sorting-sequence.md) for the detailed sequence and [plc-test-log.md](plc-test-log.md) for the validation.