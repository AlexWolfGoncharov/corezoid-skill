## Cursor Cloud specific instructions

### Project overview

This is a Python MCP (Model Context Protocol) server that exposes Corezoid API operations as tools for AI agents. There is no frontend, no database, and no Docker dependency — just a single-process Python stdio server.

### Services

| Service | Location | How to run |
|---|---|---|
| Corezoid MCP Server | `mcp-server/` | `cd mcp-server && uv run python corezoid_mcp.py` (stdio transport) |

The `claude-plugin/mcp-server/` directory contains a copy of the same MCP server packaged for Claude plugins.

### Dependencies

Dependencies are managed with `uv` (lockfile: `mcp-server/uv.lock`). Run `uv sync` inside `mcp-server/` and `claude-plugin/mcp-server/` to install.

### Linting

No linter is configured in the project. Use `ruff check` for basic Python linting:
```
ruff check mcp-server/corezoid_mcp.py claude-plugin/mcp-server/corezoid_mcp.py scripts/*.py
```

### Tests

No automated test suite exists. To verify the server works, import the module and inspect registered tools:
```
cd mcp-server && .venv/bin/python3 -c "import corezoid_mcp; print(len(corezoid_mcp.mcp._tool_manager.list_tools()), 'tools')"
```

### Environment variables

Live API calls require `COREZOID_API_LOGIN` and `COREZOID_API_SECRET`. Without them, tool invocations raise `ValueError`. See `mcp-server/README.md` for the full list.

### Non-obvious notes

- The MCP server uses **stdio** transport (not HTTP). It reads JSON-RPC from stdin and writes to stdout. Running it directly will appear to hang — this is normal; it is waiting for a client connection.
- `scripts/split_docs.py` and `scripts/extract_swagger_core_ops.py` are standalone utilities (no venv needed, stdlib only). They operate on files in `references/`.
