import json
from pathlib import Path
from typing import Any


def load_benchmark(path: str | Path) -> list[dict[str, Any]]:
    benchmark_path = Path(path)
    records: list[dict[str, Any]] = []

    with benchmark_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    return records


def describe_benchmark(path: str | Path) -> dict[str, Any]:
    records = load_benchmark(path)
    task_types = sorted({record.get("task_type", "unknown") for record in records})
    return {
        "num_records": len(records),
        "task_types": task_types,
        "status": "sample_dataset",
    }
