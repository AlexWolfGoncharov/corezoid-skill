# Corezoid MCP Server

MCP server for Corezoid API operations.

## Install

```bash
cd mcp-server
uv sync
# or: pip install mcp[cli] httpx
```

## Environment Variables

| Variable | Description |
|---|---|
| `COREZOID_API_LOGIN` | API login |
| `COREZOID_API_SECRET` | API secret |
| `COREZOID_API_BASE_URL` | API base URL (default: `https://api.corezoid.com`) |
| `COREZOID_API_VERSION` | API version (`"2"` by default, `"1"` only if required) |
| `COREZOID_COMPANY_ID` | Optional default company workspace ID |

## API key permissions (important)

For the MCP server to work, in Corezoid you must:

- **Create an API key** (it provides `login/secret` you set as `COREZOID_API_LOGIN` / `COREZOID_API_SECRET`).
- **Grant that key access to your objects** (projects/folders/processes). Without access, the API may return permission errors or appear as “not found”.

Best practice (least privilege):

- **Read + task management**: can be granted at the **whole project** level so the agent can inspect processes and **create/read/move/delete tasks**.
- **Modify (editing processes/nodes/folders)**: grant **only** to specific folders/processes you actually want the agent to change.
- **Critical processes/folders**: avoid granting **modify** to prevent accidental breakage.

## Agent Baseline

See `AGENTS.md` for AI-first operational rules that apply even without skill loading.

## Tools

Below is the full list of methods actually exposed by `mcp-server/corezoid_mcp.py` (everything decorated with `@mcp.tool()`).

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
