# repo-bootstrapper

[Русская версия](README.ru.md)

Bootstrap a new repository structure with useful defaults.

## Generated scaffold

- `README.md`
- `.gitignore`
- `pyproject.toml`
- `.github/workflows/ci.yml`
- `src/<package>/__init__.py`
- `tests/test_smoke.py`

## Usage

```bash
python3 main.py init --name my-project --target ./my-project
python3 main.py init --name my-project --target ./my-project --dry-run --format json
```

## CI usage

Use dry-run + JSON to preview generation in automation workflows.
