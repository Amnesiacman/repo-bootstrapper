import argparse
import json
from pathlib import Path

from repo_bootstrapper.scaffold import bootstrap


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="repo-bootstrapper",
        description="Generate starter repository structure",
    )
    sub = parser.add_subparsers(dest="command")
    init = sub.add_parser("init", help="Initialize project scaffold")
    init.add_argument("--name", required=True, help="Project name")
    init.add_argument("--target", required=True, help="Target directory")
    init.add_argument("--dry-run", action="store_true")
    init.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.command != "init":
        build_parser().print_help()
        return 1
    result = bootstrap(Path(args.target), args.name, dry_run=args.dry_run)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=True))
    else:
        mode = "dry-run" if result["dry_run"] else "written"
        print(f"Scaffold ready at {result['target']} ({mode})")
        for path in result["created"]:
            print(f"- {path}")
    return 0

