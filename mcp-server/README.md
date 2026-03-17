# Corezoid MCP Server

MCP-сервер для работы с Corezoid API. Даёт агенту инструменты: создание задач, изменение задач, вызов API.

English version: `README.en.md`

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

## API key и права доступа (важно)

Чтобы MCP реально работал, в Corezoid нужно:

- **Создать API Key** (он даёт `login/secret`, которые вы кладёте в `COREZOID_API_LOGIN`/`COREZOID_API_SECRET`).
- **Выдать этому ключу доступ к вашим объектам** (проектам/папкам/процессам), иначе API будет возвращать ошибки доступа или “not found”.

Рекомендованная практика (минимальные права):

- **Чтение + task management**: можно дать на **весь проект**, чтобы агент мог смотреть процессы и **создавать/читать/двигать/удалять задачи**.
- **Редактирование (modify)**: давайте **только на конкретные папки/процессы**, которые вы реально готовы доверить агенту менять.
- **Критичные процессы/папки**: **не давайте modify-доступ**, чтобы ничего случайно не сломать.

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

Ниже — полный список методов, которые реально доступны из `mcp-server/corezoid_mcp.py` (т.е. всё, что помечено `@mcp.tool()`).

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

## conv_id (ID процесса)

ID процесса можно взять из URL в Corezoid UI или из Start-ноды процесса в режиме Edit.
