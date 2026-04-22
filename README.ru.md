# repo-bootstrapper

[English version](README.md)

Генератор стартовой структуры нового репозитория с полезными настройками по умолчанию.

## Что создаётся

- `README.md`
- `.gitignore`
- `pyproject.toml`
- `.github/workflows/ci.yml`
- `src/<package>/__init__.py`
- `tests/test_smoke.py`

## Использование

```bash
python3 main.py init --name my-project --target ./my-project
python3 main.py init --name my-project --target ./my-project --dry-run --format json
```

## Использование в CI

Dry-run + JSON-режим удобно использовать для предпросмотра генерации в автоматических сценариях.
