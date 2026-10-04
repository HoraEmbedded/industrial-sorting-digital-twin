# Scripts

Utility scripts for the repository.

| File | Purpose |
| --- | --- |
| `check-repo.ps1` | Hygiene check. Fails if a tracked text file or a commit message contains an em dash, an en dash or a term that must not appear in the project. |
| `hooks/commit-msg` | Git hook that rejects commit messages containing an em dash or an en dash. |
| `clean-dashes.ps1` | Replaces em dashes and en dashes by a hyphen in the given files. Used on generated files such as the QElectroTech project. |
| `generate_wiring.py` | Draws the PLC wiring sheets (supply, inputs, outputs) from the I/O tables. Writes SVG files and an HTML file to `electrical/`. Standard library only. |
## Usage

Run the hygiene check from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\check-repo.ps1
```

Enable the versioned hooks once after cloning:

```powershell
git config core.hooksPath scripts/hooks
```