---
name: corezoid
description: "Work with Corezoid processes, nodes, task data, and API operations. Use when users ask to inspect, build, debug, or automate Corezoid workflows, including process/node logic, REF/task parameters, and MCP/API calls for create/modify/list/delete operations."
---

# Corezoid

Execute Corezoid tasks with predictable API-first workflows.

## Load References On Demand

- Start with `references/docs/INDEX.md` and open only relevant chunks in `references/docs/`.
- Use `references/docs/03-core-concepts.md` for tasks, REF, parameters, and function syntax.
- Use `references/docs/04-nodes-flow.md` to `09-nodes-callback-modify-sum.md` for node behavior.
- Use `references/Corezoid-API-reference.md` as the source of truth for raw `ops` payloads.
- Use `references/Corezoid-swagger-map.md` for operation `type` mapping and required fields.
- Use `references/playbooks/` for step-by-step implementation strategy.
- Use `references/templates/` to bootstrap new process structures quickly.
- Use `references/samples/` to copy proven patterns and payload shapes.
- Use `references/json-schema/` before finalizing process JSON and node links.
- Upstream additions (when local docs are ambiguous):
  - `https://github.com/corezoid/corezoid-ai-doc/tree/main/docs/process`
  - `https://github.com/corezoid/corezoid-ai-doc/blob/main/docs/process/process-json-validation.md`

## Required Workflow

1. Identify scope: objective, target `conv_id`, and whether company workspace needs `company_id`.
2. Inspect existing structure with `corezoid_list_process_nodes` (or `corezoid_get_process`).
3. Prefer specialized tools for tasks:
   - `corezoid_create_task`
   - `corezoid_modify_task`
   - `corezoid_delete_task`
4. For new processes, start from `references/templates/` and adapt with `references/playbooks/`.
5. Use `corezoid_api_request` only for generic or unsupported operations (folder, node, node logic, bulk edits).
6. Persist IDs from responses (`conv_id`, node `obj_id`, task `obj_id`) and reuse them.
7. Compare with nearest examples in `references/samples/` before writing complex node logic.
8. For raw `ops`, validate `type` + required fields against `references/Corezoid-swagger-map.md`.
9. Test deterministic sample input and confirm real node transitions.

## Copy Task vs Call a Process — Do NOT Confuse

- **Call a Process**: invoke process like a function, WAIT for reply. Logic type `api_rpc`. Called process must have Reply to Process node.
- **Copy Task**: send copy to another process, NO wait. Logic type `api_copy` with `mode: "create"`. Task continues in current process.
- When user wants "call process", "invoke", "get result" → Call a Process (`api_rpc`). When "fire and forget", "send copy" → Copy Task (`api_copy`).
- Avoid recursion with `api_rpc` chains; for fire-and-forget fan-out use `api_copy`.

## Node Naming and Descriptions

- Every node must have meaningful `title` and `description`.
- Avoid generic names like "Node", "Logic 1", "New node".
- Use operation-specific naming (`Validate input`, `Call payment API`, `Handle timeout`).

## Core API Conventions (Mandatory)

- Treat `REF` as required and unique per process for non-terminal task flows.
- Pass `company_id` when the process belongs to a company workspace (`i123456789` format).
- Keep explicit node positions when creating/updating multiple nodes.
- **Node modify safety:** send full payload, not partial fields (`title`, `description`, `logics`, `semaphors`, `extra`, `options`, `position` when moving).
- Apply logic transitions explicitly (`logics`) after node creation.
- Keep `obj` consistent with operation families (`conv`, `node`, `task`, `folder`), and avoid mixed payload semantics.
- **Folders:** `folder_id` = parent (0 = Root). For stage context include `stage_id`/`project_id`; if needed move via `link` op.
- Resolve API failures by checking key permissions first, then request payload structure against `references/Corezoid-API-reference.md`.

## Process Design Rules (Mandatory)

- Exactly one Start node per process; multiple End nodes are allowed and recommended.
- Keep a readable top-down layout with no node overlap.
- Give large Condition nodes more spacing; keep main/retry/error in separate visual lanes.
- Avoid transit-only nodes without business/technical purpose.
- Keep helper/retry/error-router nodes compact (`extra.modeForm = "collapse"`).
- Write readable `api_code` JavaScript and add short English comments for non-trivial steps.
- For each non-success source, create a dedicated error terminal path (no single shared final error).
- Error terminal nodes should be visually red/escalation style.
- If fake integrations are used, keep a parallel production-ready route (`api_call` or process call).

## Validation Checklist Before Finalizing

- Verify Start/End topology (single Start, reachable Ends, no accidental infinite loops).
- Validate `extra` vs `extra_type` (and similar pairs): matching keys and compatible types.
- Validate references: all `to_node_id` / `err_node_id` point to existing nodes.
- For raw API operations, re-check against `references/Corezoid-swagger-map.md`.
- Validate process JSON against `references/json-schema/` where applicable.
- Run a test task and confirm expected branch routing and error behavior.

## Project 675/679 Pattern Baseline

- Receiver/Fanout: `Start -> parse -> central router -> branch dispatch (queue/copy/rpc) -> retry/error routers -> finals`.
- Service/BL module: context load -> transform -> state write -> optional reply -> dedicated error finals.
- Communication orchestration: eligibility -> delayed sends -> per-send error handling -> final state update.
- Storage SD: minimal state process, orchestration in separate BL process.

## MCP Tools

Tools are provided by your connected Corezoid MCP server.  
Server name may vary (`corezoid`, `mcp-corezoid`, `mcp-corezoid-ma`, etc.) — use whichever Corezoid tools are available.

**Tools:** `corezoid_create_process`, `corezoid_create_task`, `corezoid_modify_task`, `corezoid_delete_task`, `corezoid_create_node`, `corezoid_modify_node`, `corezoid_get_process_version`, `corezoid_list_process_nodes`, `corezoid_get_process`, `corezoid_api_request`, `corezoid_batch_tasks`.

## Environment Variables

- `COREZOID_API_LOGIN`, `COREZOID_API_SECRET` (required)
- `COREZOID_API_BASE_URL` (default: `https://api.corezoid.com`)
- `COREZOID_API_VERSION` (default: `"2"`, recommended)
- `COREZOID_COMPANY_ID` (optional default for company workspace)
