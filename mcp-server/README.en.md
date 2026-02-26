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

## Agent Baseline

See `AGENTS.md` for AI-first operational rules that apply even without skill loading.

## Tools

- `corezoid_create_process`
- `corezoid_create_task`
- `corezoid_modify_task`
- `corezoid_delete_task`
- `corezoid_create_node`
- `corezoid_modify_node`
- `corezoid_get_process_version`
- `corezoid_list_process_nodes`
- `corezoid_get_process`
- `corezoid_api_request`
- `corezoid_batch_tasks`
