# Corezoid MCP & Skills

MCP connector and Skills for working with Corezoid through AI agents (Cursor, Claude Desktop, Codex).

## Contents

- `mcp-server/` — MCP server (tools for process, node, and task operations)
- `claude-plugin/` — Claude plugin (skill + mirrored references)
- `SKILL.md` — primary AI skill instructions
- `references/` — documentation, API reference, swagger map, playbooks, templates, samples, schema

## Quick Start

1. Configure MCP: see `mcp-server/README.md` and `mcp-server/CLAUDE-MCP-SETUP.md`
2. Set env vars: `COREZOID_API_LOGIN`, `COREZOID_API_SECRET`
3. Start using tools: `corezoid_create_task`, `corezoid_create_process`, `corezoid_api_request`, etc.

## Capabilities

- Inspect process structure (nodes, logic, parameters)
- Modify existing processes and tasks
- Create processes, folders, and nodes through API operations
