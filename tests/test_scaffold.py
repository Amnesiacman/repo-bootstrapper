from pathlib import Path

from repo_bootstrapper.scaffold import bootstrap, normalize_package_name


def test_normalize_package_name():
    assert normalize_package_name("my-app") == "my_app"


def test_bootstrap_dry_run(tmp_path: Path):
    target = tmp_path / "project"
    result = bootstrap(target, "my-app", dry_run=True)
    assert result["ok"] is True
    assert not target.exists()


def test_bootstrap_writes_files(tmp_path: Path):
    target = tmp_path / "project"
    bootstrap(target, "my-app", dry_run=False)
    assert (target / "README.md").exists()
    assert (target / "src" / "my_app" / "__init__.py").exists()

