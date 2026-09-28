# Troubleshooting Log

This document records every difficulty encountered during the project, even the smallest ones, and how they were solved. The goal is to keep a full history of the problem solving process for the portfolio and for future reference.

## Purpose

- Keep a trace of every issue, no matter how small
- Document every attempt, not only the successful one
- Identify root causes and lessons learned
- Build a reusable knowledge base for future automation projects

## Format

Each entry follows this template:

```text
### YYYY-MM-DD - Short title

- Context: where and when the issue appeared
- Symptom: what was observed
- Attempts:
  1. First attempt and result
  2. Second attempt and result
  3. ...
- Root cause: the actual cause once identified
- Solution: what finally fixed it
- Lesson learned: what to remember for next time
```

## Entries

<!-- Add new entries at the top of this section, most recent first -->

### 2026-09-28 - TIA Portal V18 installation blocked by pending file rename operations

- Context: Installation of TIA Portal V18 on Windows
- Symptom: The installer kept asking for a restart before starting, and restarting did not solve it
- Attempts:
  1. Restarted the computer and launched Start.exe again, same prompt
  2. Ran Start.exe as administrator, same prompt
  3. Inspected the Windows registry to check pending operations
- Root cause: The registry key `PendingFileRenameOperations` in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SessionManager` contained entries left by a previous installer, which made Windows believe a restart was still pending
- Solution: Opened `regedit`, navigated to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SessionManager`, deleted the `PendingFileRenameOperations` value, then relaunched `Start.exe` as administrator without restarting
- Lesson learned: Before installing Siemens software, always check this registry key. It is a well known blocker for TIA Portal installers

### 2026-09-28 - License Manager version conflict with TIA Portal V18

- Context: Installation of TIA Portal V18 on Windows
- Symptom: The installer reported a version conflict with the existing Automation License Manager
- Attempts:
  1. Tried to continue the installation with the existing License Manager, blocked
  2. Checked the version requirement of TIA Portal V18
  3. Downloaded the latest Automation License Manager from the Siemens support site
- Root cause: TIA Portal V18 requires a more recent version of Automation License Manager than the one already installed
- Solution: Installed the latest Automation License Manager first, then resumed the TIA Portal installation successfully
- Lesson learned: Always install the latest Automation License Manager before a new TIA Portal version, and check the compatibility matrix on the Siemens support site

### 2026-09-28 - Repository bootstrap on Windows

- Context: Mission 1, repository initialization on Windows
- Symptom: None, entry created to validate the format
- Attempts:
  1. Created the repository locally
  2. Added the initial folder structure
  3. Made the first commit and pushed to GitHub
- Root cause: Not applicable, this is a template entry
- Solution: Not applicable
- Lesson learned: Always check `git status` before committing
