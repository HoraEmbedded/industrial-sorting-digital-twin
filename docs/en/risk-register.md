# Risk Register

Risks identified for the project, with probability, impact and mitigation measures.

## Legend

- Probability: Low, Medium, High
- Impact: Low, Medium, High
- Status: Open, Mitigated, Closed

## Risks

### R1 - Software version mismatch

- Description: TIA Portal, PLCSIM and Factory I/O versions are not compatible
- Probability: Medium
- Impact: High
- Mitigation: Check compatibility before installation, document versions, keep installers
- Status: Open

### R2 - License unavailability

- Description: TIA Portal or Factory I/O license is missing or expired
- Probability: Medium
- Impact: High
- Mitigation: Verify licenses early, use trial versions if needed, plan a fallback
- Status: Open

### R3 - Co-simulation instability

- Description: The S7 driver loses connection between PLCSIM and Factory I/O
- Probability: Medium
- Impact: Medium
- Mitigation: Document every attempt in TROUBLESHOOTING.md, restart in a fixed order, pin versions
- Status: Open

### R4 - Windows performance limitations

- Description: The workstation is too slow to run TIA Portal, PLCSIM and Factory I/O at the same time
- Probability: Medium
- Impact: Medium
- Mitigation: Close unnecessary applications, reduce Factory I/O graphics quality, upgrade RAM if needed
- Status: Open

### R5 - I/O mapping errors

- Description: A wrong address causes the PLC to drive the wrong actuator
- Probability: Medium
- Impact: Medium
- Mitigation: Single source of truth in `docs/en/io-mapping.md`, peer review of the table, test each signal individually
- Status: Open

### R6 - Sorting logic edge cases

- Description: A box is not detected or detected twice, causing a wrong sorting
- Probability: Medium
- Impact: Medium
- Mitigation: Add debounce logic, test with different box sizes and speeds, log every cycle
- Status: Open

### R7 - Documentation drift

- Description: Documentation does not match the actual program
- Probability: Medium
- Impact: Low
- Mitigation: Update docs in the same commit as the code, review before each mission close
- Status: Open

### R8 - Time management

- Description: The project takes longer than expected
- Probability: High
- Impact: Medium
- Mitigation: Work mission by mission, one commit per step, small and verifiable deliverables
- Status: Open

## Review

- Review this register at the end of every mission
- Close risks that are no longer relevant
- Add new risks as soon as they are identified