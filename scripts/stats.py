from pathlib import Path


def collect_topic_counts(src_dir: Path) -> dict[str, int]:
    """Count solved problem modules per topic folder under src/."""
    counts: dict[str, int] = {}
    if not src_dir.exists():
        return counts
    for entry in sorted(src_dir.iterdir()):
        if entry.is_dir() and not entry.name.startswith("_"):
            files = [p for p in entry.glob("*.py") if p.name != "__init__.py"]
            counts[entry.name] = len(files)
    return counts


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    counts = collect_topic_counts(repo_root / "src")
    total = sum(counts.values())
    print(f"Total solved modules: {total}")
    for topic, count in counts.items():
        print(f"  - {topic}: {count}")


if __name__ == "__main__":
    main()
