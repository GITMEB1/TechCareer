#!/usr/bin/env python3
"""Compile Track A (Velocity) cover letter deterministically from template + JSON variables."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_KEYS = ["COMPANY_NAME", "TARGET_PAIN_POINT", "STACK_REQUIREMENT"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile Velocity Track cover letter from template and JSON substitutions")
    parser.add_argument("--input-json", required=True, help="JSON string with exactly COMPANY_NAME, TARGET_PAIN_POINT, STACK_REQUIREMENT")
    parser.add_argument("--template", default="templates/track_a_velocity_cover_letter.md", help="Template path")
    parser.add_argument("--output", required=True, help="Output file path (e.g., applications/YYYY-MM-DD-Company/cover_letter_final.md)")
    return parser.parse_args()


def load_payload(input_json: str) -> dict[str, str]:
    payload = json.loads(input_json)
    if set(payload.keys()) != set(ALLOWED_KEYS):
        raise ValueError(f"Payload must contain exactly these keys: {ALLOWED_KEYS}")

    normalized = {}
    for key in ALLOWED_KEYS:
        value = payload.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Value for {key} must be a non-empty string")
        normalized[key] = value.strip()
    return normalized


def compile_template(template_text: str, payload: dict[str, str]) -> str:
    result = template_text
    for key in ALLOWED_KEYS:
        result = result.replace("{{" + key + "}}", payload[key])
    return result


def main() -> None:
    args = parse_args()
    payload = load_payload(args.input_json)

    template_path = Path(args.template)
    if not template_path.exists():
        raise SystemExit(f"Template not found: {template_path}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content = compile_template(template_path.read_text(), payload)
    output_path.write_text(content)
    print(f"Compiled Track A cover letter: {output_path}")


if __name__ == "__main__":
    main()
