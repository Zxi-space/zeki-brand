#!/usr/bin/env python3
"""File: scripts/validate_registry.py
Purpose: 使用 JSON Schema 校验产品 Registry 的结构、字段和 ID 唯一性。
Layer: Repository / Validation Tool
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "products" / "registry.yaml"
SCHEMA_PATH = ROOT / "schemas" / "product-registry.schema.json"


def main() -> int:
    try:
        registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        print(f"ERROR: required file not found: {exc.filename}", file=sys.stderr)
        return 2
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"ERROR: failed to parse registry or schema: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(registry), key=lambda error: list(error.path))

    if errors:
        print("Product registry validation failed:")
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"- {location}: {error.message}")
        return 1

    products = registry.get("products", [])
    ids = [product["id"] for product in products]
    if len(ids) != len(set(ids)):
        print("Product registry validation failed: duplicate product id.")
        return 1

    print(f"Product registry is valid. Products: {len(products)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

