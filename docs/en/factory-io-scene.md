# Factory I/O Scene

## Scene

- Name: Sorting by Height (Advanced)
- Version: Factory I/O 2.5.10 Ultimate Edition
- Type: Pallet sorting line by height

## Physical layout

- Feeder conveyor: brings pallets to the entry conveyor
- Entry conveyor: main conveyor toward the sorting area
- Left conveyor: lane 1
- Right conveyor: lane 2
- Turntable: orients pallets before sorting
- Remover left: pusher for lane 1
- Remover right: pusher for lane 2

## Sensors

- High box: detects tall pallets
- Low box: detects short pallets
- At entry, At left entry, At left exit, At right exit: position sensors
- At load position, At unload position: loading and unloading sensors
- Pallet sensor: pallet presence sensor

## Actuators

- Entry conveyor, Feeder conveyor, Left conveyor, Right conveyor: conveyor motors
- Remover left, Remover right: pushers
- Turn: turntable command
- Green indicator, Red indicator, Yellow indicator, Reset light: indicator lights

## Emitter

The emitter is controlled by Factory I/O itself, not by the PLC. Pallets are generated automatically at a configurable rate.

## Driver

- Driver: Siemens S7-PLCSIM
- Model: S7-1200 (V14-19)

## Related documents

- `docs/en/io-mapping.md`: complete I/O mapping
- `docs/en/runbook-co-simulation.md`: co-simulation startup procedure