# Corezoid MCP Server

MCP-сервер для работы с Corezoid API. Даёт агенту инструменты: создание задач, изменение задач, вызов API.

## Установка

```bash
cd mcp-server
uv sync
# или: pip install mcp[cli] httpx
```

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `COREZOID_API_LOGIN` | API ключ (логин) |
| `COREZOID_API_SECRET` | API секрет |
| `COREZOID_API_BASE_URL` | Базовый URL API (по умолчанию: `https://api.corezoid.com`). Для self-hosted или другого инстанса укажите свой URL. |
| `COREZOID_API_VERSION` | Версия API: по умолчанию `"2"` (рекомендуется — избегает "convert to new format"). Задайте `"1"` в env только если нужна v1. |
| `COREZOID_COMPANY_ID` | Опционально, company_id для некоторых операций |

## Подключение в Cursor

1. Откройте **Cursor Settings → MCP**
2. Добавьте сервер:

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "/Users/ohancharov/Downloads/corezoid-skill/mcp-server/.venv/bin/python3",
      "args": ["/Users/ohancharov/Downloads/corezoid-skill/mcp-server/corezoid_mcp.py"],
      "env": {
        "COREZOID_API_LOGIN": "ваш_api_login",
        "COREZOID_API_SECRET": "ваш_api_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

Замените путь `/Users/ohancharov/Downloads/corezoid-skill/mcp-server` на фактический путь к папке `mcp-server`. Важно: используйте **полные пути** к python и скрипту.

## Подключение в Claude Desktop

**Подробная инструкция:** [CLAUDE-MCP-SETUP.md](CLAUDE-MCP-SETUP.md)

Кратко — в `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "/path/to/corezoid-skill/mcp-server/.venv/bin/python3",
      "args": ["/path/to/corezoid-skill/mcp-server/corezoid_mcp.py"],
      "env": {
        "COREZOID_API_LOGIN": "ваш_api_login",
        "COREZOID_API_SECRET": "ваш_api_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

## Инструкции для агента

См. [AGENTS.md](AGENTS.md) — минимальная документация для работы без skill (Copy Task vs Call a Process, workflow, переменные).

## Инструменты (Tools)

| Tool | Описание |
|------|----------|
| `corezoid_create_task` | Создать задачу в процессе |
| `corezoid_modify_task` | Изменить задачу |
| `corezoid_delete_task` | Удалить задачу |
| `corezoid_list_process_nodes` | Получить структуру процесса (ноды, логика) |
| `corezoid_get_process` | Алиас для list_process_nodes |
| `corezoid_api_request` | Произвольный запрос к API (ops array) |
| `corezoid_batch_tasks` | Пакет операций в одном запросе |

## conv_id (ID процесса)

ID процесса можно взять из URL в Corezoid UI или из Start-ноды процесса в режиме Edit.
