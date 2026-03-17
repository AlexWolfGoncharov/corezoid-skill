#!/usr/bin/env python3
"""
Corezoid MCP Server — exposes Corezoid API as tools for AI agents.

Environment variables:
  COREZOID_API_LOGIN   — API key (login)
  COREZOID_API_SECRET  — API secret
  COREZOID_API_BASE_URL — Base URL (default: https://api.corezoid.com)
  COREZOID_API_VERSION — "2" by default (all ops use v2). Set "1" in env only if v1 is required.
  COREZOID_COMPANY_ID  — Optional company_id for some operations

Usage: run with `mcp run corezoid_mcp.py` or add to Cursor/Claude MCP config.
"""

import hashlib
import json
import os
import time
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Corezoid",
    instructions="""Tools for Corezoid: create/modify tasks, processes, nodes, dashboards/charts; call API.

Required workflow:
1) Clarify objective + target conv_id/folder_id/dashboard_id and whether company_id is required.
2) Before structure edits, inspect current process via corezoid_list_process_nodes/corezoid_get_process.
3) Prefer specialized MCP tools over raw ops.
4) For raw ops, validate fields against references/Corezoid-swagger-map.md.
5) Reuse IDs from API responses (conv_id, node obj_id, task obj_id, chart obj_id).
6) Run a deterministic smoke task and verify routing.

Core conventions:
- API v2 by default (COREZOID_API_VERSION=1 only if needed).
- REF must be unique per process for non-terminal task flows.
- company_id is required for company workspaces (format i123456789).
- Folders: folder_id is parent (0=Root); in stage context include stage_id/project_id.

CRITICAL — Copy Task vs Call a Process (do NOT confuse):
- Call a Process: logic type "api_rpc", invoke and WAIT for reply; target process must contain Reply to Process node.
- Copy Task: logic type "api_copy" + mode "create", fire-and-forget, no wait.
- If user asks "invoke/get result" -> api_rpc. If "send copy/fire and forget" -> api_copy.

Node quality and safety:
- Every node must have meaningful title + description; avoid generic names like "Node", "Logic 1", "Untitled".
- For node modify/move use full payload (title, description, logics, semaphors, options, extra, and position when moving).
- Keep explicit positions when creating many nodes and apply transitions explicitly via logics.

Process design/layout discipline:
- Exactly one Start node; multiple End nodes are allowed and recommended.
- Build top-down, no overlaps, with clear lanes: main / retry / error.
- Keep vertical grid step around 120-180 and avoid edge crossings.
- Large condition/router nodes need extra spacing.
- Helper/retry/error-router nodes should be compact (extra.modeForm="collapse").
- Avoid transit-only nodes without business/technical purpose.
- If user already arranged layout in UI, preserve it unless user asks for re-layout.

Validation checklist:
- Verify Start/End topology and reachable terminals (no accidental infinite loops).
- Validate extra vs extra_type-like structures (matching keys and compatible types).
- Validate node references (to_node_id / err_node_id point to existing nodes).
- If API request fails: check permissions first, then payload structure.

Dashboards/charts:
- Prefer dedicated dashboard/chart MCP tools.
- Create charts before putting them on dashboard grid.
- Dashboard grid requires obj_id, x, y, width, height (not w/h).
- Chart modify is NOT partial: always pass obj_type + full series.
- For chart series use conv_id + node_id + title + type:"node" (state nodes: type_icon="state", type_title="Set State").
- After create/modify chart, verify series via corezoid_get_chart.

Docs: references/docs/INDEX.md and references/Corezoid-API-reference.md.""",
)

_GENERIC_NODE_TITLES = {"node", "logic", "logic 1", "new node", "untitled"}

def _get_api_version() -> str:
    """API version: "2" by default (avoids convert-to-new-format). Use v1 only via COREZOID_API_VERSION=1."""
    return os.environ.get("COREZOID_API_VERSION", "2")


def _get_base_url() -> str:
    return os.environ.get("COREZOID_API_BASE_URL", "https://api.corezoid.com").rstrip("/")


def _get_creds():
    login = os.environ.get("COREZOID_API_LOGIN")
    secret = os.environ.get("COREZOID_API_SECRET")
    if not login or not secret:
        raise ValueError(
            "Set COREZOID_API_LOGIN and COREZOID_API_SECRET environment variables"
        )
    return login, secret


def _default_company_id() -> str | None:
    value = (os.environ.get("COREZOID_COMPANY_ID") or "").strip()
    return value or None


def _with_company_id(op: dict[str, Any], company_id: str | None) -> None:
    resolved = (company_id or "").strip() or _default_company_id()
    if resolved:
        op["company_id"] = resolved


def _error_response(status_code: int, message: str, details: dict[str, Any] | None = None) -> dict:
    payload: dict[str, Any] = {
        "status_code": status_code,
        "ok": False,
        "error": message,
        "body": message,
        "json": None,
    }
    if details:
        payload["details"] = details
    return payload


def _parse_json_body(text: str) -> Any | None:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def _sign_v1(timestamp: str, content: str, secret: str) -> str:
    s = (timestamp + secret + content + secret).encode("utf-8")
    return hashlib.sha1(s).hexdigest()


def _api_request(ops: list[dict]) -> dict:
    """Send ops to Corezoid API."""
    if not isinstance(ops, list) or not ops:
        return _error_response(400, "ops must be a non-empty list of operation objects")
    if not all(isinstance(op, dict) for op in ops):
        return _error_response(400, "each op must be an object")

    try:
        login, secret = _get_creds()
    except ValueError as exc:
        return _error_response(400, str(exc))
    base = _get_base_url()
    payload = {"ops": ops}
    content = json.dumps(payload, separators=(",", ":"))
    ts = str(int(time.time()))
    sign = _sign_v1(ts, content, secret)
    url = f"{base}/api/{_get_api_version()}/json/{login}/{ts}/{sign}"
    try:
        with httpx.Client(timeout=30.0) as client:
            r = client.post(
                url,
                content=content,
                headers={"Content-Type": "application/json; charset=utf-8"},
            )
    except httpx.HTTPError as exc:
        return _error_response(502, f"Corezoid API request failed: {exc}")

    parsed = _parse_json_body(r.text)
    return {
        "status_code": r.status_code,
        "ok": 200 <= r.status_code < 300,
        "body": r.text,
        "json": parsed,
    }


def _validate_node_metadata(title: str, description: str) -> tuple[str, str]:
    normalized_title = (title or "").strip()
    normalized_description = (description or "").strip()
    if not normalized_title:
        raise ValueError("Node title is required and must be meaningful")
    if normalized_title.lower() in _GENERIC_NODE_TITLES:
        raise ValueError(
            f'Node title "{normalized_title}" is too generic. Use a descriptive title.'
        )
    if not normalized_description:
        raise ValueError("Node description is required")
    return normalized_title, normalized_description


def _extract_first_op(payload: dict[str, Any]) -> dict[str, Any]:
    ops = payload.get("ops")
    if isinstance(ops, list) and ops:
        first = ops[0]
        if isinstance(first, dict):
            return first
    return {}


def _extract_nodes_from_op(op: dict[str, Any]) -> list[dict[str, Any]]:
    nodes = op.get("nodes")
    if isinstance(nodes, list):
        return [node for node in nodes if isinstance(node, dict)]

    for key in ("conv", "obj"):
        nested = op.get(key)
        if isinstance(nested, dict):
            nested_nodes = nested.get("nodes")
            if isinstance(nested_nodes, list):
                return [node for node in nested_nodes if isinstance(node, dict)]

    return []


def _node_value(node: dict[str, Any], key: str, default: Any) -> Any:
    if key in node:
        return node.get(key, default)
    condition = node.get("condition")
    if isinstance(condition, dict) and key in condition:
        return condition.get(key, default)
    return default


def _find_node(nodes: list[dict[str, Any]], obj_id: str) -> dict[str, Any] | None:
    target = str(obj_id)
    for node in nodes:
        if (
            str(node.get("obj_id", "")) == target
            or str(node.get("id", "")) == target
            or str(node.get("node_id", "")) == target
        ):
            return node
    return None


def _resolve_version(op: dict[str, Any]) -> int | None:
    commits = op.get("commits")
    if isinstance(commits, dict):
        version = commits.get("version")
        if isinstance(version, int):
            return version
    for field in ("change_time", "create_time"):
        value = op.get(field)
        if isinstance(value, int):
            return value
    return None


def _validate_dashboard_grid(grid: list[dict[str, Any]]) -> dict | None:
    if not isinstance(grid, list):
        return _error_response(400, "grid must be a list of objects")
    required = {"obj_id", "x", "y", "width", "height"}
    for idx, item in enumerate(grid):
        if not isinstance(item, dict):
            return _error_response(400, f"grid[{idx}] must be an object")
        missing = required - set(item.keys())
        if missing:
            return _error_response(
                400,
                f"grid[{idx}] missing keys: {', '.join(sorted(missing))}",
            )
    return None


@mcp.tool()
def corezoid_create_process(
    title: str,
    description: str | None = None,
    folder_id: int | None = None,
    company_id: str | None = None,
    status: str = "active",
    create_mode: str = "without_nodes",
) -> dict:
    """Create a new Corezoid process (API v2 recommended).

    Use API v2 (default) to avoid "convert to new format" and "unconfirmed previous version".
    If folder_id/company_id fail, try corezoid_api_request with v1 format (no folder_id).

    Args:
        title: Process name.
        description: Optional description.
        folder_id: Folder ID (v2; required in some workspaces).
        company_id: Company ID, e.g. 'i7856235891' (v2).
        status: active | paused | debug | blocked (per API docs).
        create_mode: without_nodes (v2) or omit for v1.
    """
    op: dict[str, Any] = {
        "type": "create",
        "obj": "conv",
        "title": title,
        "description": description or "",
        "status": status,
    }
    if folder_id is not None:
        op["folder_id"] = folder_id
    _with_company_id(op, company_id)
    if _get_api_version() == "2":
        op["conv_type"] = "process"
        op["create_mode"] = create_mode
    return _api_request([op])


@mcp.tool()
def corezoid_create_dashboard(
    title: str,
    folder_id: int,
    project_id: int | None = None,
    stage_id: int | None = None,
    description: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Create a Corezoid dashboard.

    Required for dashboards: title + folder_id. For stage folders, include project_id + stage_id.

    Args:
        title: Dashboard title.
        folder_id: Target folder ID (parent).
        project_id: Project ID (required if folder is inside a project/stage).
        stage_id: Stage ID (required if folder is inside a project/stage).
        description: Optional description.
        company_id: Optional company ID.
    """
    op: dict[str, Any] = {
        "type": "create",
        "obj": "dashboard",
        "title": title,
        "description": description or "",
        "folder_id": folder_id,
    }
    if project_id is not None:
        op["project_id"] = project_id
    if stage_id is not None:
        op["stage_id"] = stage_id
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_dashboard(
    obj_id: int,
    company_id: str | None = None,
) -> dict:
    """Show dashboard details (including grid and chart_list)."""
    op: dict[str, Any] = {
        "type": "show",
        "obj": "dashboard",
        "obj_id": obj_id,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_modify_dashboard(
    obj_id: int,
    title: str | None = None,
    description: str | None = None,
    time_range: dict[str, Any] | None = None,
    grid: list[dict[str, Any]] | None = None,
    company_id: str | None = None,
) -> dict:
    """Modify dashboard metadata and layout.

    Grid items MUST use keys: obj_id, x, y, width, height (not w/h).
    If grid is provided, validate keys to avoid "grid.width" API errors.

    Args:
        obj_id: Dashboard ID.
        title: Optional title (recommended to keep current).
        description: Optional description.
        time_range: Optional dict, e.g. {"timezone_offset":-180,"select":"online"}.
        grid: Optional list of grid items with chart obj_id + coordinates.
        company_id: Optional company ID.
    """
    if grid is not None:
        err = _validate_dashboard_grid(grid)
        if err:
            return err
    op: dict[str, Any] = {
        "type": "modify",
        "obj": "dashboard",
        "obj_id": obj_id,
    }
    if title is not None:
        op["title"] = title
    if description is not None:
        op["description"] = description
    if time_range is not None:
        op["time_range"] = time_range
    if grid is not None:
        op["grid"] = grid
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_create_chart(
    dashboard_id: int,
    obj_type: str,
    name: str,
    series: list[dict[str, Any]],
    description: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Create a dashboard chart.

    Required: dashboard_id, obj_type (table|column|pie|funnel), name, series.
    Series items must include:
      - conv_id, node_id, title
      - type: "node"
      - type_icon: "state" and type_title: "Set State" for state nodes
    """
    op: dict[str, Any] = {
        "type": "create",
        "obj": "chart",
        "dashboard_id": dashboard_id,
        "obj_type": obj_type,
        "name": name,
        "series": series,
        "description": description or "",
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_get_chart(
    dashboard_id: int,
    obj_id: str,
    company_id: str | None = None,
) -> dict:
    """Get chart details (verifies series is populated)."""
    op: dict[str, Any] = {
        "type": "get",
        "obj": "chart",
        "dashboard_id": dashboard_id,
        "obj_id": obj_id,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_modify_chart(
    dashboard_id: int,
    obj_id: str,
    obj_type: str,
    name: str,
    series: list[dict[str, Any]],
    description: str | None = None,
    sort: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Modify a chart.

    Chart modify is NOT partial. Always send obj_type + full series,
    otherwise API returns "Key 'obj_type' is required" or "Key 'series' is required".
    """
    op: dict[str, Any] = {
        "type": "modify",
        "obj": "chart",
        "dashboard_id": dashboard_id,
        "obj_id": obj_id,
        "obj_type": obj_type,
        "name": name,
        "series": series,
        "description": description or "",
    }
    if sort is not None:
        op["sort"] = sort
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_conv(obj_id: int, company_id: str | None = None) -> dict:
    """Show a process (conv) by id."""
    op = {"type": "show", "obj": "conv", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_modify_conv(
    obj_id: int,
    title: str | None = None,
    description: str | None = None,
    status: str | None = None,
    folder_id: int | None = None,
    company_id: str | None = None,
) -> dict:
    """Modify a process (conv).

    Supports renaming, changing status, or moving to another folder.
    """
    op: dict[str, Any] = {"type": "modify", "obj": "conv", "obj_id": obj_id}
    if title is not None:
        op["title"] = title
    if description is not None:
        op["description"] = description
    if status is not None:
        op["status"] = status
    if folder_id is not None:
        op["folder_id"] = folder_id
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_list_convs(
    obj: str = "conv",
    filters: dict[str, Any] | None = None,
    company_id: str | None = None,
) -> dict:
    """List processes.

    Args:
        obj: Typically "conv".
        filters: Optional additional fields supported by Corezoid list (e.g., folder_id).
    """
    op: dict[str, Any] = {"type": "list", "obj": obj}
    if filters:
        op.update(filters)
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_delete_conv(obj_id: int, company_id: str | None = None) -> dict:
    """Move a process to trash."""
    op = {"type": "delete", "obj": "conv", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_restore_conv(obj_id: int, company_id: str | None = None) -> dict:
    """Restore a trashed process."""
    op = {"type": "restore", "obj": "conv", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_destroy_conv(obj_id: int, company_id: str | None = None) -> dict:
    """Permanently delete a process."""
    op = {"type": "destroy", "obj": "conv", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_favorite_conv(
    obj_id: int,
    favorite: bool,
    company_id: str | None = None,
) -> dict:
    """Toggle process favorite flag."""
    op = {"type": "favorite", "obj": "conv", "obj_id": obj_id, "favorite": favorite}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_link_conv(
    obj_id: int,
    obj_to: int,
    privs: list[dict[str, Any]],
    company_id: str | None = None,
) -> dict:
    """Link a process to another object (share/permissions via privs)."""
    op = {
        "type": "link",
        "obj": "conv",
        "obj_id": obj_id,
        "obj_to": obj_to,
        "privs": privs,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_create_folder(
    title: str,
    folder_id: int = 0,
    stage_id: int | None = None,
    project_id: int | None = None,
    company_id: str | None = None,
) -> dict:
    """Create a folder.

    folder_id is the parent (0 = Root). For stage folders, include stage_id (or stage_short_name) and project_id.
    """
    op: dict[str, Any] = {"type": "create", "obj": "folder", "title": title, "folder_id": folder_id}
    if stage_id is not None:
        op["stage_id"] = stage_id
    if project_id is not None:
        op["project_id"] = project_id
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_modify_folder(
    obj_id: int,
    title: str | None = None,
    description: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Modify folder title/description."""
    op: dict[str, Any] = {"type": "modify", "obj": "folder", "obj_id": obj_id}
    if title is not None:
        op["title"] = title
    if description is not None:
        op["description"] = description
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_folder(obj_id: int, company_id: str | None = None) -> dict:
    """Show folder details."""
    op = {"type": "show", "obj": "folder", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_list_folder(obj_id: int, company_id: str | None = None) -> dict:
    """List folder contents by folder id."""
    op = {"type": "list", "obj": "folder", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_link_folder(
    obj_id: int,
    folder_id: int,
    parent_id: int,
    company_id: str | None = None,
) -> dict:
    """Move a folder using link (obj_type: folder)."""
    op = {
        "type": "link",
        "obj": "folder",
        "obj_id": obj_id,
        "obj_type": "folder",
        "folder_id": folder_id,
        "parent_id": parent_id,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_favorite_folder(obj_id: int, favorite: bool, company_id: str | None = None) -> dict:
    """Toggle folder favorite flag."""
    op = {"type": "favorite", "obj": "folder", "obj_id": obj_id, "favorite": favorite}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_delete_folder(obj_id: int, company_id: str | None = None) -> dict:
    """Move folder to trash."""
    op = {"type": "delete", "obj": "folder", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_restore_folder(obj_id: int, company_id: str | None = None) -> dict:
    """Restore a trashed folder."""
    op = {"type": "restore", "obj": "folder", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_destroy_folder(obj_id: int, company_id: str | None = None) -> dict:
    """Permanently delete a folder."""
    op = {"type": "destroy", "obj": "folder", "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_node(
    conv_id: int,
    obj_id: str,
    company_id: str | None = None,
) -> dict:
    """Show node details by node id."""
    op = {"type": "show", "obj": "node", "conv_id": conv_id, "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_list_node_tasks(
    conv_id: int,
    obj_id: str,
    limit: int | None = None,
    company_id: str | None = None,
) -> dict:
    """List tasks currently in a node (by node id)."""
    op: dict[str, Any] = {"type": "list", "obj": "node", "conv_id": conv_id, "obj_id": obj_id}
    if limit is not None:
        op["limit"] = limit
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_delete_node(conv_id: int, obj_id: str, company_id: str | None = None) -> dict:
    """Delete node by id."""
    op = {"type": "delete", "obj": "node", "conv_id": conv_id, "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_reset_node(conv_id: int, obj_id: str, company_id: str | None = None) -> dict:
    """Reset node counters."""
    op = {"type": "reset", "obj": "node", "conv_id": conv_id, "obj_id": obj_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_list_nodes(pattern: str, company_id: str | None = None) -> dict:
    """List nodes by pattern across workspace."""
    op = {"type": "list", "obj": "nodes", "pattern": pattern}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_task(
    conv_id: int,
    ref: str | None = None,
    obj_id: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Show a task by ref or obj_id."""
    if not ref and not obj_id:
        return _error_response(400, "Provide ref or obj_id to show a task")
    op: dict[str, Any] = {"type": "show", "obj": "task", "conv_id": conv_id}
    if ref is not None:
        op["ref"] = ref
    if obj_id is not None:
        op["obj_id"] = obj_id
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_task_from_archive(
    conv_id: int,
    ref: str | None = None,
    obj_id: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Show a task from archive by ref or obj_id.

    Corezoid UI can store tasks in an archive (typically until end of month).
    This tool wraps the raw API op used for reading archived tasks.
    """
    if not ref and not obj_id:
        return _error_response(400, "Provide ref or obj_id to show a task from archive")
    op: dict[str, Any] = {"type": "show", "obj": "task", "conv_id": conv_id, "archive": 1}
    if ref is not None:
        op["ref"] = ref
    if obj_id is not None:
        op["obj_id"] = obj_id
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_step_task_next(
    conv_id: int,
    obj_id: str,
    data: dict[str, Any],
    company_id: str | None = None,
) -> dict:
    """Move task to next node (step_next)."""
    op = {"type": "step_next", "obj": "task", "conv_id": conv_id, "obj_id": obj_id, "data": data}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_step_task_prev(
    conv_id: int,
    obj_id: str,
    data: dict[str, Any],
    company_id: str | None = None,
) -> dict:
    """Move task to previous node (step_prev)."""
    op = {"type": "step_prev", "obj": "task", "conv_id": conv_id, "obj_id": obj_id, "data": data}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_step_task_goto(
    conv_id: int,
    obj_id: str,
    data: dict[str, Any],
    company_id: str | None = None,
) -> dict:
    """Move task to a specific node (step_goto)."""
    op = {"type": "step_goto", "obj": "task", "conv_id": conv_id, "obj_id": obj_id, "data": data}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_confirm_commit(conv_id: int, version: int, company_id: str | None = None) -> dict:
    """Confirm commit (version) for a process."""
    op = {"type": "confirm", "obj": "commit", "conv_id": conv_id, "version": version}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_show_commit(conv_id: int, version: int, company_id: str | None = None) -> dict:
    """Show commit by version for a process."""
    op = {"type": "show", "obj": "commit", "conv_id": conv_id, "version": version}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_delete_commit(
    version: int,
    obj_id: int,
    obj_type: str,
    company_id: str | None = None,
) -> dict:
    """Delete a commit (dangerous; use with care)."""
    op = {"type": "delete", "obj": "commit", "version": version, "obj_id": obj_id, "obj_type": obj_type}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_list_commits(conv_id: int, company_id: str | None = None) -> dict:
    """List commits for a process."""
    op = {"type": "list", "obj": "commits", "conv_id": conv_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_create_task(
    conv_id: int,
    ref: str,
    data: dict[str, Any],
    company_id: str | None = None,
) -> dict:
    """Create a new task in a Corezoid process.

    Args:
        conv_id: Process ID (conv_id). Can be found in process URL or Start node.
        ref: Unique task reference within the process. Use getRandomRef or unique string.
        data: Task parameters as JSON object (key-value pairs).
        company_id: Optional company ID (e.g. 'i111111222').
    """
    op = {
        "type": "create",
        "conv_id": conv_id,
        "obj": "task",
        "data": data,
        "ref": ref,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_modify_task(
    conv_id: int,
    ref: str,
    data: dict[str, Any],
    company_id: str | None = None,
) -> dict:
    """Modify an existing task in a Corezoid process.

    Args:
        conv_id: Process ID.
        ref: Task reference (REF) to modify.
        data: New/updated parameters for the task.
        company_id: Optional company ID.
    """
    op = {
        "type": "modify",
        "conv_id": conv_id,
        "obj": "task",
        "data": data,
        "ref": ref,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_delete_task(
    conv_id: int,
    obj_id: str,
    node_id: str | None = None,
    company_id: str | None = None,
) -> dict:
    """Delete a task from a Corezoid process.

    Args:
        conv_id: Process ID.
        obj_id: Task ID (obj_id from create/modify response).
        node_id: Optional node ID where the task is located.
        company_id: Optional company ID.
    """
    op = {
        "type": "delete",
        "obj": "task",
        "conv_id": conv_id,
        "obj_id": obj_id,
    }
    if node_id:
        op["node_id"] = node_id
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_create_node(
    conv_id: int,
    obj_type: int,
    version: int,
    title: str = "",
    description: str = "",
    company_id: str | None = None,
) -> dict:
    """Create a new node in a Corezoid process.

    Per API docs: type, obj, conv_id, version, obj_type are required.
    Get version from corezoid_list_process_nodes response (commits.version or change_time).

    IMPORTANT: Always provide a meaningful title and description for each node — makes processes easier to understand and debug. Avoid generic names like "Node".

    Args:
        conv_id: Process ID.
        obj_type: 0=normal/logic, 1=start, 2=final, 3=escalation.
        version: Process version (unix timestamp from list response).
        title: Node title (required, descriptive — e.g. "Validate user", "Call payment API").
        description: Node description (what the node does — for easier process review later).
        company_id: Optional company ID.
    """
    validated_title, validated_description = _validate_node_metadata(title, description)

    op: dict[str, Any] = {
        "type": "create",
        "obj": "node",
        "conv_id": conv_id,
        "version": version,
        "obj_type": obj_type,
        "title": validated_title,
        "description": validated_description,
    }
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_modify_node(
    conv_id: int,
    obj_id: str,
    obj_type: int,
    logics: list[dict[str, Any]] | None = None,
    version: int | None = None,
    position: list[int] | None = None,
    title: str | None = None,
    description: str | None = None,
    semaphors: list[dict[str, Any]] | None = None,
    extra: dict[str, Any] | None = None,
    options: dict[str, Any] | None = None,
    company_id: str | None = None,
) -> dict:
    """Modify a node: set position, logics, etc.

    Per API docs: type, obj, conv_id, obj_id, obj_type, logics are required.
    Get version from corezoid_list_process_nodes (commits.version).
    For position-only update, pass current logics from node (or [] if empty).

    IMPORTANT — logics types for inter-process:
    - Call a Process (invoke, wait for reply): type "api_rpc", conv_id, etc.
    - Copy Task (send copy, no wait): type "api_copy", mode "create".
    Do NOT use api_copy when user wants "call process" / "invoke and get result".

    Also enforces full-node payload safety: if some fields are omitted, the tool
    auto-loads current node snapshot and merges missing fields before modify.

    Args:
        conv_id: Process ID.
        obj_id: Node ID (24-char string from create response).
        obj_type: 0=normal, 1=start, 2=final, 3=escalation.
        logics: Array of logic rules, e.g. [{"type":"go","to_node_id":"..."}]. If omitted, keeps current logics.
        version: Process version (required for optimistic locking).
        position: [x, y] coordinates.
        title: Node title. If omitted, keeps current title from process snapshot.
        description: Node description. If omitted, keeps current description from process snapshot.
        semaphors: Node semaphors. If omitted, keeps current semaphors.
        extra: Node extra object. If omitted, keeps current extra.
        options: Node options object. If omitted, keeps current options.
        company_id: Optional company ID.
    """
    if position is not None and (len(position) != 2):
        return _error_response(400, "position must contain exactly two coordinates [x, y]")

    current_snapshot = corezoid_list_process_nodes(conv_id, company_id)
    if current_snapshot["status_code"] != 200:
        return current_snapshot

    payload = current_snapshot.get("json")
    if not isinstance(payload, dict):
        return {
            "status_code": 500,
            "ok": False,
            "error": "Failed to parse process snapshot before node modify",
            "body": "Failed to parse process snapshot before node modify",
            "json": None,
        }

    first_op = _extract_first_op(payload)
    nodes = _extract_nodes_from_op(first_op)
    node = _find_node(nodes, obj_id)
    if not node:
        return {
            "status_code": 404,
            "body": f'Node "{obj_id}" not found in process {conv_id}',
        }

    resolved_title = title if title is not None else str(node.get("title") or "")
    resolved_description = (
        description if description is not None else str(node.get("description") or "")
    )
    validated_title, validated_description = _validate_node_metadata(
        resolved_title, resolved_description
    )

    resolved_logics = logics if logics is not None else _node_value(node, "logics", [])
    resolved_semaphors = (
        semaphors if semaphors is not None else _node_value(node, "semaphors", [])
    )
    resolved_extra = extra if extra is not None else _node_value(node, "extra", {})
    resolved_options = options if options is not None else _node_value(node, "options", {})

    resolved_version = version if version is not None else _resolve_version(first_op)

    op: dict[str, Any] = {
        "type": "modify",
        "obj": "node",
        "conv_id": conv_id,
        "obj_id": obj_id,
        "obj_type": obj_type,
        "title": validated_title,
        "description": validated_description,
        "logics": resolved_logics,
        "semaphors": resolved_semaphors,
        "extra": resolved_extra,
        "options": resolved_options,
    }
    if resolved_version is not None:
        op["version"] = resolved_version
    if position is not None:
        op["position"] = position
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_get_process_version(conv_id: int, company_id: str | None = None) -> dict:
    """Get process version (required for create/modify node operations).

    Returns version from list response: commits.version or change_time.
    Use this before corezoid_create_node or corezoid_modify_node.

    Args:
        conv_id: Process ID.
        company_id: Optional company ID.
    """
    result = corezoid_list_process_nodes(conv_id, company_id)
    if result["status_code"] != 200:
        return result
    data = result.get("json")
    if isinstance(data, dict):
        ops = data.get("ops", [])
        if ops:
            op = ops[0]
            commits = op.get("commits", {})
            version = commits.get("version")
            if version is None:
                version = op.get("change_time") or op.get("create_time") or int(time.time())
            return {
                "status_code": 200,
                "ok": True,
                "version": version,
                "body": result["body"],
                "json": data,
            }
    return result


@mcp.tool()
def corezoid_list_process_nodes(conv_id: int, company_id: str | None = None) -> dict:
    """Get process structure with all nodes (list of nodes, logics, obj_type).

    Use this to understand process logic: node titles, types, connections (logics).
    Returns API response with status_code and body (JSON string).
    Version for node ops: commits.version or change_time in response.

    Args:
        conv_id: Process ID (conv_id).
        company_id: Optional company ID (required for some workspaces).
    """
    op: dict[str, Any] = {"type": "list", "obj": "conv", "obj_id": conv_id}
    _with_company_id(op, company_id)
    return _api_request([op])


@mcp.tool()
def corezoid_get_process(conv_id: int, company_id: str | None = None) -> dict:
    """Get process info. Prefer corezoid_list_process_nodes for full structure (nodes, logics).

    Falls back to list operation — Corezoid API uses type 'list' for conv, not 'get'.

    Args:
        conv_id: Process ID.
        company_id: Optional company ID (try if request fails without it).
    """
    return corezoid_list_process_nodes(conv_id, company_id)


@mcp.tool()
def corezoid_api_request(ops: list[dict[str, Any]]) -> dict:
    """Send a raw Corezoid API request (ops array).

    Use for operations not covered by other tools: get process, list tasks,
    folder operations, etc. See Corezoid API docs for ops format.

    Node logics: Call a Process = api_rpc (invoke, wait). Copy Task = api_copy, mode create (send copy, no wait).

    Example ops:
      - create task: {"type":"create","conv_id":123,"obj":"task","ref":"x","data":{}}
      - modify task: {"type":"modify","conv_id":123,"obj":"task","ref":"x","data":{}}
      - get conv: {"type":"list","obj":"conv","obj_id":123}

    Returns:
      - status_code: HTTP status code
      - ok: True for 2xx response
      - body: raw text response
      - json: parsed JSON response if valid, else null
    """
    return _api_request(ops)


@mcp.tool()
def corezoid_batch_tasks(operations: list[dict[str, Any]]) -> dict:
    """Execute multiple Corezoid operations in one API call.

    Each item in operations should be a valid op (create, modify, delete task, etc.).
    """
    return _api_request(operations)


if __name__ == "__main__":
    mcp.run()
