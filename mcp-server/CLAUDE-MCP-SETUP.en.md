# Corezoid MCP Setup for Claude Desktop

## 1) Requirements

- Claude Desktop
- `uv` (recommended) or Python 3.10+
- Corezoid API credentials (`COREZOID_API_LOGIN`, `COREZOID_API_SECRET`)

## 2) Install Dependencies

```bash
cd /path/to/corezoid-skill/mcp-server
uv sync
```

Without `uv`:

```bash
pip install mcp httpx
```

## 3) Claude Config File

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

## 4) Add MCP Server

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "/path/to/corezoid-skill/mcp-server/.venv/bin/python3",
      "args": ["/path/to/corezoid-skill/mcp-server/corezoid_mcp.py"],
      "env": {
        "COREZOID_API_LOGIN": "your_api_login",
        "COREZOID_API_SECRET": "your_api_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

## 5) Verify

1. Restart Claude Desktop completely.
2. Open a new chat.
3. Confirm Corezoid tools are visible.
4. Run a small test action (for example: create a test task).
