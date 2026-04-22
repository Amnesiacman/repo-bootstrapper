from pathlib import Path


def normalize_package_name(name: str) -> str:
    return name.strip().replace("-", "_")


def build_files(project_name: str) -> dict:
    package_name = normalize_package_name(project_name)
    return {
        "README.md": f"# {project_name}\n\nBootstrapped with repo-bootstrapper.\n",
        ".gitignore": "__pycache__/\n*.pyc\n.pytest_cache/\n",
        "pyproject.toml": (
            "[project]\n"
            f'name = "{project_name}"\n'
            'version = "0.1.0"\n'
            'requires-python = ">=3.10"\n\n'
            "[build-system]\n"
            'requires = ["setuptools>=69", "wheel"]\n'
            'build-backend = "setuptools.build_meta"\n'
        ),
        ".github/workflows/ci.yml": (
            "name: ci\n\n"
            "on:\n"
            "  push:\n"
            "    branches: [main]\n"
            "  pull_request:\n\n"
            "jobs:\n"
            "  test:\n"
            "    runs-on: ubuntu-latest\n"
            "    steps:\n"
            "      - uses: actions/checkout@v4\n"
            "      - uses: actions/setup-python@v5\n"
            "        with:\n"
            '          python-version: "3.11"\n'
            "      - run: python -m pip install --upgrade pip pytest\n"
            "      - run: python -m pytest\n"
        ),
        f"src/{package_name}/__init__.py": "",
        "tests/test_smoke.py": "def test_smoke():\n    assert True\n",
    }


def bootstrap(target: Path, project_name: str, dry_run: bool = False) -> dict:
    files = build_files(project_name)
    planned = []
    for rel, content in files.items():
        p = target / rel
        planned.append(str(p))
        if not dry_run:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
    return {
        "ok": True,
        "target": str(target),
        "project_name": project_name,
        "dry_run": dry_run,
        "created": planned,
    }

