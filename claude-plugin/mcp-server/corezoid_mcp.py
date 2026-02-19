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
    instructions="""Tools for Corezoid: create/modify tasks, processes, nodes; call API.

Key conventions:
- API v2 by default (COREZOID_API_VERSION=1 only if needed).
- REF: unique per process for non-terminal tasks.
- company_id: required for company workspace (format i123456789).

CRITICAL — Copy Task vs Call a Process (do NOT confuse):
- Call a Process: invoke process like a function, WAIT for reply. Use logic type "api_rpc". Called process MUST have Reply to Process node.
- Copy Task: send copy to another process, NO wait. Use logic type "api_copy" with mode "create". Task continues in current process.
When user wants "call process" or "invoke and get result" → Call a Process (api_rpc). When "fire and forget" or "send copy" → Copy Task (api_copy).

Node naming: Always give each node a meaningful title and description. Avoid generic names like "Node"; use descriptive names (e.g. "Validate user", "Call payment API") so processes are easier to understand later.

Folders: folder_id = parent (0 = Root). If parent is in stage, add stage_id and project_id to create. If create puts folder in Root, move via link op (obj_type: "folder", folder_id, parent_id). See Corezoid-API-reference.md.

Docs: references/docs/INDEX.md for navigation. references/Corezoid-API-reference.md for ops format.""",
)

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


def _sign_v1(timestamp: str, content: str, secret: str) -> str:
    s = (timestamp + secret + content + secret).encode("utf-8")
    return hashlib.sha1(s).hexdigest()


def _api_request(ops: list[dict]) -> dict:
    """Send ops to Corezoid API."""
    login, secret = _get_creds()
    base = _get_base_url()
    payload = {"ops": ops}
    content = json.dumps(payload, separators=(",", ":"))
    ts = str(int(time.time()))
    sign = _sign_v1(ts, content, secret)
    url = f"{base}/api/{_get_api_version()}/json/{login}/{ts}/{sign}"
    with httpx.Client(timeout=30.0) as client:
        r = client.post(url, content=content)
    return {"status_code": r.status_code, "body": r.text}


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
    if company_id:
        op["company_id"] = company_id
    if _get_api_version() == "2":
        op["conv_type"] = "process"
        op["create_mode"] = create_mode
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
    if company_id:
        op["company_id"] = company_id
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
    if company_id:
        op["company_id"] = company_id
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
    if company_id:
        op["company_id"] = company_id
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
    op: dict[str, Any] = {
        "type": "create",
        "obj": "node",
        "conv_id": conv_id,
        "version": version,
        "obj_type": obj_type,
        "title": title or "Node",
        "description": description or "",
    }
    if company_id:
        op["company_id"] = company_id
    return _api_request([op])


@mcp.tool()
def corezoid_modify_node(
    conv_id: int,
    obj_id: str,
    obj_type: int,
    logics: list[dict[str, Any]],
    version: int | None = None,
    position: list[int] | None = None,
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

    Args:
        conv_id: Process ID.
        obj_id: Node ID (24-char string from create response).
        obj_type: 0=normal, 1=start, 2=final, 3=escalation.
        logics: Array of logic rules, e.g. [{"type":"go","to_node_id":"..."}].
        version: Process version (required for optimistic locking).
        position: [x, y] coordinates.
        company_id: Optional company ID.
    """
    op: dict[str, Any] = {
        "type": "modify",
        "obj": "node",
        "conv_id": conv_id,
        "obj_id": obj_id,
        "obj_type": obj_type,
        "logics": logics,
    }
    if version is not None:
        op["version"] = version
    if position is not None:
        op["position"] = position
    if company_id:
        op["company_id"] = company_id
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
    try:
        data = json.loads(result["body"])
        ops = data.get("ops", [])
        if ops:
            op = ops[0]
            commits = op.get("commits", {})
            version = commits.get("version")
            if version is None:
                version = op.get("change_time") or op.get("create_time") or int(time.time())
            return {"status_code": 200, "version": version, "body": result["body"]}
    except (json.JSONDecodeError, KeyError):
        pass
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
    if company_id:
        op["company_id"] = company_id
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
