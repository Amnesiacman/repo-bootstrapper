import json
from pathlib import Path

from repo_bootstrapper.cli import main


def test_cli_json_dry_run(tmp_path: Path, capsys):
    target = tmp_path / "project"
    code = main(
        ["init", "--name", "demo", "--target", str(target), "--dry-run", "--format", "json"]
    )
    payload = json.loads(capsys.readouterr().out.strip())
    assert code == 0
    assert payload["dry_run"] is True


def test_cli_writes(tmp_path: Path):
    target = tmp_path / "project"
    code = main(["init", "--name", "demo", "--target", str(target)])
    assert code == 0
    assert (target / "README.md").exists()

