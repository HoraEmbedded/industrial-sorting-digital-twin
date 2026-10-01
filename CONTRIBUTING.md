# Contributing

This project is primarily a personal portfolio project. Contributions are welcome in the form of issues, discussions or pull requests.

## Commit convention

This repository follows the Conventional Commits specification.

Examples:

- `feat: add sorting logic FB`
- `fix: correct I/O mapping for pusher 1`
- `docs: update architecture diagram`
- `chore: update gitignore`

## Branching

- `main` is the stable branch
- Feature branches use the pattern `feat/<short-description>`
- Fix branches use the pattern `fix/<short-description>`

## Style

- English for code, comments, documentation and commits
- No em dashes in any file or commit message
- UTF-8 encoding without BOM


## Language policy

- Documentation is written in English first. French translations live in `docs/fr` and `README.fr.md`.
- Folder README files are English only.
- Commit messages are in English and follow Conventional Commits (feat, fix, docs, chore, refactor, test).

## Style rules

- No em dashes or en dashes in any file or commit message. Use a comma, a colon, parentheses or a plain hyphen instead.
- Files are saved as UTF-8 (see `.editorconfig`).
- Run `powershell -ExecutionPolicy Bypass -File scripts\check-repo.ps1` before pushing.

## Git hooks

Enable the versioned hooks once after cloning:

```powershell
git config core.hooksPath scripts/hooks
```