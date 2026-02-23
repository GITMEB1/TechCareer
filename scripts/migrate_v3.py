#!/usr/bin/env python3
"""Idempotent migration for opportunity schema v3.

Adds:
- deployment_track
- life_fit_score
- logistics_clearance

Preserves all existing and deprecated keys.
"""

from __future__ import annotations

from pathlib import Path
import re
import yaml

TRACKING_FILE = Path("tracking/opportunities.yaml")

SALARY_FLOOR_GBP = 50000


def infer_track(category: str) -> str:
    return "Pivot" if str(category).upper() == "DATA" else "Velocity"


def parse_salary_floor(salary_range: str) -> tuple[bool, bool]:
    """Return (known, meets_floor)."""
    text = str(salary_range or "").strip()
    if not text or text.lower() == "unknown":
        return False, False

    numbers = [int(n) for n in re.findall(r"(\d{2,3})k", text.lower())]
    if not numbers:
        raw = [int(n.replace(",", "")) for n in re.findall(r"(\d{2,3}(?:,\d{3})?)", text)]
        numbers = [n // 1000 if n >= 1000 else n for n in raw]

    if not numbers:
        return False, False

    highest = max(numbers)
    return True, highest >= (SALARY_FLOOR_GBP // 1000)


def infer_commute_viable(work_style: str, location: str) -> bool:
    ws = str(work_style or "").lower()
    loc = str(location or "").lower()
    if "remote" in ws or "remote" in loc:
        return True
    if "hybrid" in ws or "manchester" in loc:
        return True
    return False


def infer_remote_flexibility(work_style: str) -> str:
    ws = str(work_style or "").lower()
    if "remote" in ws:
        return "Remote"
    if "hybrid" in ws:
        return "Hybrid"
    if "onsite" in ws:
        return "Onsite"
    return "Unknown"


def migrate_entry(entry: dict) -> bool:
    changed = False

    if "deployment_track" not in entry or entry.get("deployment_track") in (None, ""):
        entry["deployment_track"] = infer_track(entry.get("category", "Unknown"))
        changed = True

    if "life_fit_score" not in entry or not isinstance(entry.get("life_fit_score"), int):
        fit_score = entry.get("fit_score", 0)
        try:
            entry["life_fit_score"] = int(fit_score)
        except Exception:
            entry["life_fit_score"] = 0
        changed = True

    lc = entry.get("logistics_clearance")
    if not isinstance(lc, dict):
        lc = {}
        entry["logistics_clearance"] = lc
        changed = True

    known_salary, salary_met = parse_salary_floor(entry.get("salary_range", "Unknown"))

    if "salary_floor_met" not in lc:
        lc["salary_floor_met"] = salary_met if known_salary else False
        changed = True

    if "commute_viable" not in lc:
        lc["commute_viable"] = infer_commute_viable(entry.get("work_style", ""), entry.get("location", ""))
        changed = True

    if "remote_flexibility" not in lc:
        lc["remote_flexibility"] = infer_remote_flexibility(entry.get("work_style", ""))
        changed = True

    return changed


def main() -> None:
    if not TRACKING_FILE.exists():
        raise SystemExit(f"Missing file: {TRACKING_FILE}")

    data = yaml.safe_load(TRACKING_FILE.read_text()) or {}
    opportunities = data.get("opportunity_list", [])
    if not isinstance(opportunities, list):
        raise SystemExit("Invalid tracking format: 'opportunity_list' must be a list")

    changed_count = 0
    for entry in opportunities:
        if isinstance(entry, dict) and migrate_entry(entry):
            changed_count += 1

    TRACKING_FILE.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    print(f"Migration complete. Updated {changed_count} entries out of {len(opportunities)}.")


if __name__ == "__main__":
    main()
