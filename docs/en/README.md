# Documentation (English)

English is the reference language of this repository. French translations are listed in [docs/fr](../fr/README.md).

## Project definition

| Document | Description | Status |
| :--- | :--- | :---: |
| [scope.md](scope.md) | Scope definition | Completed |
| [functional-specs.md](functional-specs.md) | Functional specifications | Completed |
| [assumptions-and-constraints.md](assumptions-and-constraints.md) | Technical assumptions and constraints | Completed |
| [milestone-plan.md](milestone-plan.md) | Milestone plan | Completed |
| [risk-register.md](risk-register.md) | Risk register | Maintained |

## Architecture and mapping

| Document | Description | Status |
| :--- | :--- | :---: |
| [io-mapping.md](io-mapping.md) | Single source of truth for the link between Factory I/O and PLC addresses. | **Completed** |
| [plc-architecture.md](plc-architecture.md) | Controller details, signal polarities, block layout, gating rules. | **Completed** |
| [sorting-sequence.md](sorting-sequence.md) | Sorting sequence, GRAFCET, transitions, routing rules. | **Completed** |
| [scene-behavior.md](scene-behavior.md) | Documented experiments profiling the turntable, sensors and emitter. | **Completed** |
| [factory-io-scene.md](factory-io-scene.md) | Factory I/O scene configuration and component list. | **Completed** |
| [architecture.md](architecture.md) | High level architecture overview. | Completed |
| [architecture-diagram.md](architecture-diagram.md) | Mermaid diagram of the system layers. | Completed |
| [electrical-design.md](electrical-design.md) | Electrical design basis for the wiring schematic. | **Completed** |

## Environment and operation

| Document | Description | Status |
| :--- | :--- | :---: |
| [software-versions.md](software-versions.md) | Software versions reference. | Completed |
| [environment-audit.md](environment-audit.md) | Workstation environment audit. | Completed |
| [tool-checklist.md](tool-checklist.md) | Tool startup and shutdown checklist. | Completed |
| [runbook-co-simulation.md](runbook-co-simulation.md) | Co-simulation startup procedure. | Completed |

## Testing

| Document | Description | Status |
| :--- | :--- | :---: |
| [plc-test-log.md](plc-test-log.md) | Full PLC test log: **29 tests** in three groups (13 modes and safety, 12 sorting logic, 4 pipelined emission), all validated. | **Passed (100%)** |

## Related files

- [Troubleshooting log](../../TROUBLESHOOTING.md)
- [Changelog](../../CHANGELOG.md)