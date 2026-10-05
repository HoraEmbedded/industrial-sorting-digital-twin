# Factory I/O Scene

## Scene

- Name: Sorting by Height (Advanced)
- Version: Factory I/O 2.5.10 Ultimate Edition
- Type: Box sorting line by height, with a turntable

## Physical layout

- Feeder conveyor: brings boxes from the emitter to the entry conveyor
- Entry conveyor: main conveyor toward the turntable
- Turntable: orients boxes before sorting, rotates 90 degrees clockwise
- Left conveyor: exit lane for low boxes
- Right conveyor: exit lane for high boxes
- Remover left: deletes boxes at the end of the left exit conveyor
- Remover right: deletes boxes at the end of the right exit conveyor

## Sensors

- High box: top beam of the light curtain. TRUE only for high boxes.
- Low box: bottom beam of the light curtain. TRUE for both low and high boxes.
- At entry: photocell at the output of the emitter.
- At back: rear sensor of the entry area.
- At front: queue sensor in front of the turntable.
- At turntable entry: reflective sensor at the center of the turntable, used for centering.
- At load position: limit switch, TRUE when the turntable is at its home position (aligned with the entry conveyor).
- At unload position: limit switch, TRUE when the turntable has completed its 90 degree rotation.
- At left entry, at right entry: confirm a box has engaged on the left or right exit conveyor.
- At left exit, at right exit: normally closed, drop to FALSE when a box reaches the end of the conveyor.

## Actuators

- Feeder conveyor, entry conveyor, left conveyor, right conveyor: conveyor motors.
- Load: runs the turntable rollers forward, pulls a box in and pushes it to the right exit.
- Unload: runs the turntable rollers backward, pushes a box to the left exit.
- Turn: rotates the turntable 90 degrees clockwise. Returns home when released.
- Remover left, remover right: end of line removers, delete boxes from the scene.
- Emit: pulse that generates one box at the emitter. See the Emitter section below.
- Green, yellow, red indicators, and the pushbutton lamps: operator signalling.

## Emitter

The emitter is controlled by the PLC through `Q_Emit`, not by Factory I/O. A pulse of 500 ms on `Q_Emit` generates one box. Holding `Q_Emit` TRUE generates boxes continuously with a fixed spacing, but the sorting sequence only uses single pulses, one per cycle (see sorting-sequence.md).

The emitter is configured in the scene to produce two part types:
- `Box (S)`, a low box, which triggers only the low beam of the light curtain.
- `Box (L)`, a high box, which triggers both beams.

The distribution is random. No pallets or other part types are selected.

## Driver

- Driver: Siemens S7-PLCSIM
- Model: S7-1200 (V14-19)

## Related documents

- `docs/en/io-mapping.md`: complete I/O mapping, single source of truth.
- `docs/en/scene-behavior.md`: sensor and actuator experiments that define the sorting sequence.
- `docs/en/sorting-sequence.md`: sequence and routing rules.
- `docs/en/runbook-co-simulation.md`: co-simulation startup procedure.