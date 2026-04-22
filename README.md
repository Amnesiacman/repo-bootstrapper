# repo-bootstrapper

`repo-bootstrapper` создает базовую структуру нового репозитория с полезными настройками для CI-ready старта.

## Что генерирует v0.1

- `README.md`
- `.gitignore`
- `pyproject.toml`
- `.github/workflows/ci.yml`
- `src/<package_name>/__init__.py`
- `tests/test_smoke.py`

## Использование

```bash
python3 -m pip install -e .
repo-bootstrapper init --name my-project --target ./my-project
```

Dry-run (без записи файлов):

```bash
repo-bootstrapper init --name my-project --target ./my-project --dry-run --format json
```
