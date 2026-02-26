# Corezoid MCP Agent Baseline

Minimum baseline rules for an agent working with Corezoid through MCP without a separate skill.

## 1) Baseline Workflow

1. Clarify the objective and context first: target `conv_id`, and whether company workspace requires `company_id`.
2. Before process-structure edits, always fetch the current snapshot with `corezoid_list_process_nodes`.
3. For task operations, use specialized tools: `corezoid_create_task`, `corezoid_modify_task`, `corezoid_delete_task`.
4. For unsupported or generic operations, use `corezoid_api_request` and validate payloads against `references/Corezoid-API-reference.md`.

## 2) Mandatory API Conventions

- Use API v2 by default (`COREZOID_API_VERSION=2`).
- `REF` must be unique within a process for active task flows.
- For company workspace, pass `company_id` (`i123456789`).
- For folders: `folder_id` is the parent folder (`0` = Root). In stage context include `stage_id` / `project_id`.

## 3) Nodes and Safe Modifications

- Do not confuse:
  - **Call a Process**: `api_rpc`, waits for reply.
  - **Copy Task**: `api_copy` + `mode: "create"`, no wait.
- Each node must have meaningful `title` and `description`.
- For node modify/move, send full payload (at minimum: `title`, `description`, `logics`, `semaphors`, `options`, `extra`, and `position` when moving) to avoid metadata loss.

## 4) Process Design and Readability

- Build process flow top-down without node overlaps.
- Keep main/retry/error in separate visual lanes.
- For technical helper nodes, prefer compact mode (`extra.modeForm = "collapse"`).

## 5) Structure Validation

- Before finalization, validate `extra` / `extra_type` style structures (matching keys and compatible types).
- For raw `ops`, verify operation `type` and required fields with `references/Corezoid-swagger-map.md`.
- If a request fails, check API-key permissions first, then payload structure.
