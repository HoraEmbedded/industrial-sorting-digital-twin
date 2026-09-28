# I/O Mapping

Mapping between PLCSIM and Factory I/O.

## Inputs

| Address | Signal                        | Type |
|---------|-------------------------------|------|
| %I0.0   | Start button (NO)             | BOOL |
| %I0.1   | Stop button (NC)              | BOOL |
| %I0.2   | Emergency stop (NC)           | BOOL |
| %I0.3   | Mode selector (1 auto, 0 man) | BOOL |
| %I0.4   | Entry sensor                  | BOOL |
| %I0.5   | Size sensor low               | BOOL |
| %I0.6   | Size sensor high              | BOOL |
| %I0.7   | Pusher 1 retracted sensor     | BOOL |
| %I1.0   | Part evacuated lane 1         | BOOL |
| %I1.1   | Part evacuated lane 2         | BOOL |

## Outputs

| Address | Signal                        | Type |
|---------|-------------------------------|------|
| %Q0.0   | Green light (running)         | BOOL |
| %Q0.1   | Red light (stopped or fault)  | BOOL |
| %Q0.2   | Main conveyor motor           | BOOL |
| %Q0.3   | Lane 1 conveyor motor         | BOOL |
| %Q0.4   | Lane 2 conveyor motor         | BOOL |
| %Q0.5   | Pusher 1 command              | BOOL |
| %Q0.6   | Pusher 2 command              | BOOL |

See ../fr/ for the French version (available at the end of the project).