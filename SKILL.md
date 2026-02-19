---
name: corezoid
description: "Work with Corezoid processes, nodes, task data, and API operations. Use when users ask to inspect, build, debug, or automate Corezoid workflows, including process/node logic, REF/task parameters, and MCP/API calls for create/modify/list/delete operations."
---

# Corezoid

Execute Corezoid tasks with predictable API-first workflows.

## Load References On Demand

- **Start with** `references/docs/INDEX.md` — navigation guide: which file to open for each topic (nodes, parameters, API, etc.). Do not load the full `Corezoid-documentation.md`; use the chunked docs in `references/docs/`.
- Use `references/docs/03-core-concepts.md` for concepts, task parameters, REF semantics, `{{conv[...].ref[...]}}`, functions.
- Use `references/docs/04-nodes-flow.md` through `09-nodes-callback-modify-sum.md` for specific node behavior (Start, End, Condition, Code, API Call, Queue, etc.).
- Use `references/Corezoid-API-reference.md` before any low-level `corezoid_api_request` call; treat it as the source of truth for `ops` payloads.
- Use `references/Corezoid-swagger-map.md` for Swagger-derived `type` mappings and required fields per operation.
- If a user provides a new Swagger file, regenerate the map:
  - `python3 scripts/extract_swagger_core_ops.py /path/to/swagger.json -o references/Corezoid-swagger-map.md`

## Follow This Workflow

1. Identify scope first: objective, `conv_id`, and whether a company workspace requires `company_id`.
2. Inspect existing structure with `corezoid_list_process_nodes` (or `corezoid_get_process`).
3. Prefer specialized tools for task data operations:
   - `corezoid_create_task`
   - `corezoid_modify_task`
   - `corezoid_delete_task`
4. Create processes with `corezoid_create_process` (API v2 by default) to avoid "convert to new format" and "unconfirmed previous version".
5. Use `corezoid_api_request` only for generic or unsupported operations (folder, node, node logic, bulk edits).
6. Persist IDs from responses (`conv_id`, node `obj_id`, task `obj_id`) and reuse them in follow-up operations.
7. Test with deterministic sample input via `corezoid_create_task` and confirm node transition behavior.
8. For raw `ops`, validate `type` and required fields against `references/Corezoid-swagger-map.md` before sending requests.

## Copy Task vs Call a Process — Do NOT Confuse

- **Call a Process**: invoke process like a function, WAIT for reply. Logic type `api_rpc`. Called process must have Reply to Process node.
- **Copy Task**: send copy to another process, NO wait. Logic type `api_copy` with `mode: "create"`. Task continues in current process.
- When user wants "call process", "invoke", "get result" → Call a Process (`api_rpc`). When "fire and forget", "send copy" → Copy Task (`api_copy`).

## Node Naming and Descriptions

- **Always** give each node a meaningful `title` (name) when creating or modifying.
- **Always** add a `description` explaining what the node does — this makes processes easier to understand and debug later.
- Avoid generic names like "Node" or "Logic 1"; use descriptive names (e.g. "Validate user", "Call payment API").

## Enforce Core API Conventions

- Treat `REF` as required and unique per process for non-terminal task flows.
- Pass `company_id` when the process belongs to a company workspace (`i123456789` format).
- Keep node positions explicit when creating/updating multiple nodes to avoid overlap in the visual editor.
- When creating or restructuring processes, always lay out nodes as a logical top-down flowchart (top to bottom), with clear vertical progression from Start to End and readable spacing between levels.
- Apply logic transitions explicitly (`logics`) after node creation; do not assume default routing.
- Keep `obj` consistent with operation families (`conv`, `node`, `task`, `folder`), and avoid mixed payload semantics.
- **Folders:** `folder_id` = parent (0 = Root). If parent is in stage, add `stage_id` and `project_id` to create. If create puts folder in Root, move via `link` op (obj_type: "folder", folder_id, parent_id). See `references/Corezoid-API-reference.md`.
- Resolve API failures by checking key permissions first, then request payload structure against `references/Corezoid-API-reference.md`.

## Use MCP Server Configuration

- Read setup and env requirements in `mcp-server/README.md`.
- Use:
  - `COREZOID_API_LOGIN`
  - `COREZOID_API_SECRET`
  - `COREZOID_API_BASE_URL` (optional override)
  - `COREZOID_API_VERSION` (default: "2" — recommended to avoid format conversion errors)
