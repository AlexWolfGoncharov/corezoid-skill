# Corezoid Plugin для Claude Code и Claude Cowork

Плагин добавляет **skill** (знания и инструкции) для работы с Corezoid. MCP не входит в плагин — используется ваш уже подключённый MCP Corezoid.

## Как это работает

1. **Плагин** — даёт skill (когда и как работать с Corezoid).
2. **MCP** — вы подключаете отдельно в настройках Cursor / Claude Desktop / Claude Code. Имя может быть любым: `corezoid`, `mcp-corezoid`, `mcp-corezoid-ma`, `mcp-corezoid-az` и т.д.
3. Claude использует skill и инструменты из вашего MCP Corezoid.

## Подключение MCP (обязательно)

Добавьте MCP Corezoid в глобальные настройки (имя на ваш выбор):

### Claude Desktop — `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "/path/to/corezoid-skill/mcp-server/.venv/bin/python3",
      "args": ["/path/to/corezoid-skill/mcp-server/corezoid_mcp.py"],
      "env": {
        "COREZOID_API_LOGIN": "ваш_login",
        "COREZOID_API_SECRET": "ваш_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

### Cursor — Settings → MCP

Тот же блок `corezoid` в `mcpServers`.

### Claude Code

MCP настраивается в конфиге Claude Code (аналогично).

**Важно:** имя сервера может быть любым (`corezoid`, `mcp-corezoid`, `mcp-corezoid-ma`, `mcp-corezoid-az` и т.д.) — skill использует доступные инструменты Corezoid.

## Установка плагина

### Claude Code

```bash
claude --plugin-dir /path/to/corezoid-skill/claude-plugin
```

### Claude Cowork

Plugins → Add plugin → путь к папке `claude-plugin`.

## Структура плагина

```
claude-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── corezoid/
│       ├── SKILL.md
│       └── references/
├── mcp-server/              # Код MCP (для настройки вручную)
│   ├── corezoid_mcp.py
│   └── pyproject.toml
└── README.md
```

Папка `mcp-server/` — для справки. Путь к ней указывайте в конфиге MCP.
