# Architecture

This document describes the software architecture of the PLC program and the digital twin.

## PLC program structure (TIA Portal)

- OB1 Main: main cycle and block calls
- FB1 / DB1 Gestion_Modes: safety, start and stop, emergency stop
- FB2 / DB2 Logique_Tri: sorting sequence in LAD or GRAPH
- FC1 Affectation_IO: I/O mapping between Factory I/O and PLCSIM

## Digital twin (Factory I/O)

- Sorting by size scene
- Conveyors, pushers, photoelectric sensors
- Co-simulation with PLCSIM via the Siemens driver

## Status

To be completed during the project.