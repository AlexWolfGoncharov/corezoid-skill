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

## MCP Routing By Corezoid URL

Pick MCP server by URL host before any Corezoid operation:

- `https://corezoid.theroarbank.in/...` -> `mcp-corezoid-in`
- `https://corezoid-main.theroarbank.in/...` -> `mcp-corezoid-main-in`
- `https://corezoid.prod.liobank.vn/...` -> `mcp-corezoid-vn`
- `https://corezoid.prod.liobank.vn/...` with company workspace requiring `company_id=i570824777` -> `mcp-corezoid-vn-343`
- `https://corezoid.leobank.az/...` -> `mcp-corezoid-az`
- `https://corezoid-crm.leobank.az/...` -> `mcp-corezoid-az-crm`
- `https://corezoid.creditplus.ma/...` -> `corezoid` (MA)

If the user gives a Corezoid link, parse its host and use the mapped MCP server for all operations in that task.

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

## Dashboards & Charts (Corezoid UI)

- Dashboard ops use `obj: "dashboard"` with `type: create|modify|show`.
- Dashboard `grid` items require keys `obj_id`, `x`, `y`, `width`, `height` (not `w/h`). Missing `grid.width` causes validation errors.
- Charts are separate objects: `obj: "chart"`. Create/modify charts before placing them in the dashboard grid.
- Chart `create`/`modify` required fields:
  - `dashboard_id`, `obj_type` (`table` | `column` | `pie` | `funnel`), `name`, `series`.
  - `series` items must include `conv_id` + `node_id` + `title`, and `type: "node"` (use `type_icon: "state"` and `type_title: "Set State"` for state nodes).
- Chart `modify` is not partial: include `obj_type` and full `series`, otherwise API returns `Key 'obj_type' is required` or `Key 'series' is required`.
- After create, always `get` the chart and verify `series` is populated; if empty, re-`modify` with full `series`.

## MCP Playbook: Dashboards & Charts

Use `corezoid_api_request` (or the host-mapped MCP server) for dashboards and charts. Always include `company_id` for company workspaces.

1) Show an existing dashboard
```
{"ops":[{"type":"show","obj":"dashboard","obj_id":184,"company_id":"<company_id>"}]}
```

2) Create a dashboard (place it in a folder)
```
{"ops":[{"type":"create","obj":"dashboard","company_id":"<company_id>","project_id":<project_id>,"stage_id":<stage_id>,"folder_id":<folder_id>,"title":"<title>","description":"<optional>"}]}
```

3) Create charts (always pass full `series`)
```
{"ops":[{"type":"create","obj":"chart","company_id":"<company_id>","dashboard_id":<dashboard_id>,"obj_type":"column","name":"<chart name>","series":[{"title":"other","conv_id":<conv_id>,"node_id":"<node_id>","type":"node","type_icon":"state","type_title":"Set State"}]}]}
```

4) Modify chart name or series (must include `obj_type` + full `series`)
```
{"ops":[{"type":"modify","obj":"chart","company_id":"<company_id>","dashboard_id":<dashboard_id>,"obj_id":"<chart_id>","obj_type":"column","name":"<chart name>","series":[{"title":"S-1","conv_id":<conv_id>,"node_id":"<node_id>","type":"node","type_icon":"state","type_title":"Set State"}]}]}
```

5) Place charts on a dashboard (grid uses width/height)
```
{"ops":[{"type":"modify","obj":"dashboard","company_id":"<company_id>","obj_id":<dashboard_id>,"title":"<title>","description":"<desc>","time_range":{"timezone_offset":-180,"select":"online"},"grid":[{"obj_id":"<chart_id>","x":0,"y":0,"width":4,"height":4}]}]}
```

6) Verify chart content (should return `series`)
```
{"ops":[{"type":"get","obj":"chart","company_id":"<company_id>","dashboard_id":<dashboard_id>,"obj_id":"<chart_id>"}]}
```

Notes:
- If `get` returns empty `series`, re-run `modify` with the full series.
- `grid` errors about `grid.width` mean you used `w/h` instead of `width/height`.

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

## Layout Pattern Memory (IN Cashback)

- For mixed business + queue orchestration, use 3 visual lanes:
  - Main lane (`x` about `120`): `Start -> Route Source -> Derive -> Lookup -> Validate -> Accrue -> Validate Cashback -> CRM -> Final Success`.
  - Queue lane (`x` about `740-860`): `Trigger Queue Reader -> Queue Intake -> Final Queued`.
- Queue error lane (`x` about `1100-1250`): `Reader Trigger Error Router -> Final Reader Trigger Error`.
- Keep vertical step around `120-180` and avoid lane crossing where possible.
- If user manually adjusted node coordinates in UI, treat that layout as canonical and preserve it in further edits unless user asks to re-layout.
- Throttled dequeue pattern: if reader process uses `api_get_task` on source process queue node, source `Queue Intake` can route directly to business logic (`go -> Derive/...`), and reader does not need `api_copy` back.

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

## Use MCP Server Configuration

- Read setup and env requirements in `mcp-server/README.md`.
- Use:
  - `COREZOID_API_LOGIN`
  - `COREZOID_API_SECRET`
  - `COREZOID_API_BASE_URL` (optional override)
  - `COREZOID_API_VERSION` (default: "2" — recommended to avoid format conversion errors)
  - `COREZOID_COMPANY_ID` (optional default for company workspace)

## MCP Tool Catalog

This is the complete tool surface exposed by `mcp-server/corezoid_mcp.py` (everything decorated with `@mcp.tool()`).

| Tool | What it does |
|------|--------------|
| `corezoid_create_process` | Create a new Corezoid process (API v2 recommended). |
| `corezoid_create_dashboard` | Create a Corezoid dashboard. |
| `corezoid_show_dashboard` | Show dashboard details (including grid and chart_list). |
| `corezoid_modify_dashboard` | Modify dashboard metadata and layout. |
| `corezoid_create_chart` | Create a dashboard chart. |
| `corezoid_get_chart` | Get chart details (verifies series is populated). |
| `corezoid_modify_chart` | Modify a chart. |
| `corezoid_show_conv` | Show a process (conv) by id. |
| `corezoid_modify_conv` | Modify a process (conv). |
| `corezoid_list_convs` | List processes. |
| `corezoid_delete_conv` | Move a process to trash. |
| `corezoid_restore_conv` | Restore a trashed process. |
| `corezoid_destroy_conv` | Permanently delete a process. |
| `corezoid_favorite_conv` | Toggle process favorite flag. |
| `corezoid_link_conv` | Link a process to another object (share/permissions via privs). |
| `corezoid_create_folder` | Create a folder. |
| `corezoid_modify_folder` | Modify folder title/description. |
| `corezoid_show_folder` | Show folder details. |
| `corezoid_list_folder` | List folder contents by folder id. |
| `corezoid_link_folder` | Move a folder using link (obj_type: folder). |
| `corezoid_favorite_folder` | Toggle folder favorite flag. |
| `corezoid_delete_folder` | Move folder to trash. |
| `corezoid_restore_folder` | Restore a trashed folder. |
| `corezoid_destroy_folder` | Permanently delete a folder. |
| `corezoid_show_node` | Show node details by node id. |
| `corezoid_list_node_tasks` | List tasks currently in a node (by node id). |
| `corezoid_delete_node` | Delete node by id. |
| `corezoid_reset_node` | Reset node counters. |
| `corezoid_list_nodes` | List nodes by pattern across workspace. |
| `corezoid_show_task` | Show a task by ref or obj_id. |
| `corezoid_show_task_from_archive` | Show a task from archive by ref or obj_id. |
| `corezoid_step_task_next` | Move task to next node (step_next). |
| `corezoid_step_task_prev` | Move task to previous node (step_prev). |
| `corezoid_step_task_goto` | Move task to a specific node (step_goto). |
| `corezoid_confirm_commit` | Confirm commit (version) for a process. |
| `corezoid_show_commit` | Show commit by version for a process. |
| `corezoid_delete_commit` | Delete a commit (dangerous; use with care). |
| `corezoid_list_commits` | List commits for a process. |
| `corezoid_create_task` | Create a new task in a Corezoid process. |
| `corezoid_modify_task` | Modify an existing task in a Corezoid process. |
| `corezoid_delete_task` | Delete a task from a Corezoid process. |
| `corezoid_create_node` | Create a new node in a Corezoid process. |
| `corezoid_modify_node` | Modify a node: set position, logics, etc. |
| `corezoid_get_process_version` | Get process version (required for create/modify node operations). |
| `corezoid_list_process_nodes` | Get process structure with all nodes (list of nodes, logics, obj_type). |
| `corezoid_get_process` | Get process info. Prefer corezoid_list_process_nodes for full structure (nodes, logics). |
| `corezoid_api_request` | Send a raw Corezoid API request (ops array). |
| `corezoid_batch_tasks` | Execute multiple Corezoid operations in one API call. |
