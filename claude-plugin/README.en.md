# Corezoid Plugin for Claude

This plugin provides a Corezoid skill.  
MCP server is connected separately in Cursor / Claude Desktop / Claude Code settings.

## How It Works

1. Plugin provides skill instructions and references.
2. MCP server provides executable tools.
3. Agent combines both for reliable Corezoid operations.

## MCP Requirement

Configure an MCP server entry (name can be arbitrary):

## API key permissions (important)

For the MCP server to work with your processes/tasks, in Corezoid you must:

- **Create an API key** and set its `login/secret` in MCP env (`COREZOID_API_LOGIN` / `COREZOID_API_SECRET`).
- **Grant the API key access** to your objects (projects/folders/processes). Otherwise the agent won’t be able to “see” them and the API may return permission errors.

Best practice (least privilege):

- **Read + task management**: can be granted at the **whole project** level so the agent can inspect processes and manage tasks.
- **Modify (editing)**: grant only to the folders/processes you explicitly want the agent to change.
- **Critical processes/folders**: avoid granting **modify** to prevent accidental breakage.

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "/path/to/corezoid-skill/mcp-server/.venv/bin/python3",
      "args": ["/path/to/corezoid-skill/mcp-server/corezoid_mcp.py"],
      "env": {
        "COREZOID_API_LOGIN": "your_login",
        "COREZOID_API_SECRET": "your_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

## Plugin Structure

- `.claude-plugin/plugin.json`
- `skills/corezoid/SKILL.md`
- `skills/corezoid/references/` (docs, API refs, playbooks, templates, samples, schema)
- `mcp-server/` (local MCP implementation copy)
