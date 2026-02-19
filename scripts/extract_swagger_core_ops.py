#!/usr/bin/env python3
"""Generate a compact Corezoid API ops map from an OpenAPI/Swagger file."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head", "trace"}
CORE_TAGS = ["conv", "convs", "node", "nodes", "task", "folder", "commit", "commits", "company"]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def ref_name(ref: str) -> str:
    return ref.split("/")[-1]


def resolve_schema(schema: dict, all_schemas: dict, depth: int = 0) -> dict:
    if depth > 15:
        return {}
    if "$ref" in schema:
        target = all_schemas.get(ref_name(schema["$ref"]), {})
        return resolve_schema(target, all_schemas, depth + 1)
    return schema


def extract_required_for_ref(schema_ref: str, all_schemas: dict) -> list[str]:
    name = ref_name(schema_ref)
    schema = resolve_schema(all_schemas.get(name, {}), all_schemas)
    required = schema.get("required", [])
    return [str(x) for x in required]


def op_request_items(op: dict) -> dict:
    content = (op.get("requestBody") or {}).get("content", {})
    app_json = content.get("application/json", {})
    schema = app_json.get("schema", {})
    return (((schema.get("properties") or {}).get("ops") or {}).get("items") or {})


def collect_ops(spec: dict) -> list[dict]:
    rows: list[dict] = []
    for path, item in (spec.get("paths") or {}).items():
        for method, op in (item or {}).items():
            if method.lower() not in HTTP_METHODS:
                continue
            tags = op.get("tags") or []
            rows.append(
                {
                    "path": path,
                    "method": method.upper(),
                    "tag": tags[0] if tags else "",
                    "operation_id": op.get("operationId", ""),
                    "summary": op.get("summary", ""),
                    "op": op,
                }
            )
    return rows


def render_markdown(spec: dict) -> str:
    info = spec.get("info") or {}
    servers = spec.get("servers") or []
    schemas = (spec.get("components") or {}).get("schemas") or {}
    security = (spec.get("components") or {}).get("securitySchemes") or {}
    rows = collect_ops(spec)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines: list[str] = []
    lines.append("# Corezoid Swagger Ops Map")
    lines.append("")
    lines.append(f"Generated from `swagger.json` on {generated} (UTC).")
    lines.append("")
    lines.append("## API Shape")
    lines.append("")
    lines.append(f"- OpenAPI: `{spec.get('openapi', '-')}`")
    lines.append(f"- API title: `{info.get('title', '-')}`")
    lines.append(f"- API version: `{info.get('version', '-')}`")
    if servers:
        lines.append(f"- Default server: `{servers[0].get('url', '-')}`")
    lines.append(f"- Total paths: `{len(spec.get('paths') or {})}`")
    lines.append(
        "- Core request envelope for JSON operations: `{\"ops\": [ { ...operation... } ]}`"
    )
    lines.append("")
    lines.append("## Authentication (from Swagger)")
    lines.append("")
    if security:
        for name, sch in security.items():
            lines.append(f"- `{name}`: type `{sch.get('type', '-')}`")
            if sch.get("name"):
                lines.append(f"  - credential placeholder in path: `{sch['name']}`")
            if sch.get("in"):
                lines.append(f"  - location: `{sch['in']}`")
    else:
        lines.append("- No security schemes were declared.")
    lines.append("")
    lines.append("## Core Ops By Tag")
    lines.append("")
    lines.append("Use this section when composing `ops` for `corezoid_api_request`.")
    lines.append("")

    for tag in CORE_TAGS:
        tag_rows = [r for r in rows if r["tag"] == tag]
        if not tag_rows:
            continue
        lines.append(f"### `{tag}`")
        lines.append("")
        for row in tag_rows:
            lines.append(
                f"- `{row['method']} {row['path']}` (`operationId`: `{row['operation_id']}`)"
            )
            items = op_request_items(row["op"])
            discriminator = items.get("discriminator") or {}
            mapping = discriminator.get("mapping") or {}
            if mapping:
                lines.append("  - supported `type` values and key required fields:")
                for type_name, schema_ref in mapping.items():
                    req = extract_required_for_ref(schema_ref, schemas)
                    req_text = ", ".join(req) if req else "(no required list in schema)"
                    lines.append(f"    - `{type_name}`: `{req_text}`")
        lines.append("")

    lines.append("## Swagger-Driven Guardrails")
    lines.append("")
    lines.append("- Keep `obj` aligned with tag intent (`conv`, `node`, `task`, `folder`).")
    lines.append("- For process/node/task mutations, always include all required fields from the mapped schema.")
    lines.append("- Prefer declared `type` values from the discriminator mapping; avoid guessing unsupported `type` names.")
    lines.append("- If tool wrappers differ from Swagger enums (for example process status naming), verify with current workspace behavior before bulk changes.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("swagger", type=Path, help="Path to swagger/openapi JSON file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Output markdown file path",
    )
    args = parser.parse_args()

    spec = load_json(args.swagger)
    output = render_markdown(spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
