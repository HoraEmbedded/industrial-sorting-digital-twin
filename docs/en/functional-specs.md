# Functional Specifications

## Modes

- Manual mode
- Automatic mode

## Automatic mode

- Press START to run the conveyors
- Press STOP to stop the system at the end of the cycle
- Emergency stop cuts all actuators immediately

## Sorting logic

- Entry sensor detects incoming box
- Size detection:
  - High sensor = 0 and low sensor = 1: small box
  - High sensor = 1 and low sensor = 1: large box
- Pusher is activated when the part is aligned
- End of lane sensor increments the corresponding counter

## Status

To be completed during the project.
See ../fr/ for the French version (available at the end of the project).