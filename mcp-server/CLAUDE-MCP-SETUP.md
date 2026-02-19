# Подключение Corezoid MCP в Claude

Пошаговая инструкция для Claude Desktop.

---

## 1. Требования

- **Claude Desktop** — [claude.ai/download](https://claude.ai/download)
- **uv** (рекомендуется) или **Python 3.10+**
- **API-ключи Corezoid** — в Corezoid: Users & Groups → Create → API key

---

## 2. Установка зависимостей

```bash
cd /path/to/corezoid-skill/mcp-server
uv sync
```

Если `uv` нет:
```bash
pip install mcp httpx
```

---

## 3. Файл конфигурации Claude

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

Если файла нет — создайте его.

---

## 4. Добавьте Corezoid MCP

Откройте `claude_desktop_config.json` и добавьте (или дополните) секцию `mcpServers`.

**Рекомендуемый вариант** — прямой вызов Python из venv (избегает ошибок с путями):

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "/Users/ohoncharov/Downloads/corezoid-skill/mcp-server/.venv/bin/python3",
      "args": [
        "/Users/ohoncharov/Downloads/corezoid-skill/mcp-server/corezoid_mcp.py"
      ],
      "env": {
        "COREZOID_API_LOGIN": "ваш_api_login",
        "COREZOID_API_SECRET": "ваш_api_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

**Вариант с uv** (если путь к скрипту — полный):

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/Users/ohoncharov/Downloads/corezoid-skill/mcp-server",
        "python",
        "/Users/ohoncharov/Downloads/corezoid-skill/mcp-server/corezoid_mcp.py"
      ],
      "env": {
        "COREZOID_API_LOGIN": "ваш_api_login",
        "COREZOID_API_SECRET": "ваш_api_secret",
        "COREZOID_API_BASE_URL": "https://api.corezoid.com"
      }
    }
  }
}
```

**Замените:**
- `/Users/ohoncharov/Downloads/corezoid-skill/mcp-server` — на ваш полный путь к папке `mcp-server`
- `ваш_api_login` — логин API-ключа
- `ваш_api_secret` — секрет API-ключа

**Self-hosted Corezoid:**
```json
"COREZOID_API_BASE_URL": "https://your-corezoid-instance.com"
```

---

## 5. Вариант без uv (системный Python)

Если `uv` не установлен — используйте **полный путь** к скрипту:

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "python3",
      "args": [
        "/Users/ohoncharov/Downloads/corezoid-skill/mcp-server/corezoid_mcp.py"
      ],
      "env": {
        "COREZOID_API_LOGIN": "ваш_api_login",
        "COREZOID_API_SECRET": "ваш_api_secret"
      }
    }
  }
}
```

Сначала установите зависимости:
```bash
cd /Users/ohoncharov/Downloads/corezoid-skill/mcp-server
pip install mcp httpx
```

---

## 6. Проверка

1. Полностью закройте Claude Desktop и запустите снова.
2. Создайте новый чат.
3. В чате должны появиться инструменты Corezoid (иконка скрепки или меню инструментов).
4. Напишите, например: «Создай тестовую задачу в процессе 12345 с параметром test: hello».

---

## 7. Несколько MCP-серверов

Если уже есть другие MCP:

```json
{
  "mcpServers": {
    "corezoid": {
      "command": "uv",
      "args": ["run", "--project", "/path/to/mcp-server", "python", "corezoid_mcp.py"],
      "env": {
        "COREZOID_API_LOGIN": "...",
        "COREZOID_API_SECRET": "..."
      }
    },
    "другой_сервер": {
      "command": "...",
      "args": ["..."]
    }
  }
}
```

---

## 8. Ошибки

**`can't open file '//corezoid_mcp.py'`**
- Используйте **полный путь** к скрипту в `args`, например: `"/Users/.../mcp-server/corezoid_mcp.py"`.
- Или переключитесь на вариант с `.venv/bin/python3` (раздел 4).

**MCP не появляется**
- Проверьте путь к `mcp-server` (должен вести к папке с `corezoid_mcp.py` и `pyproject.toml`).
- Убедитесь, что `uv sync` или `pip install` выполнены без ошибок.

**"Set COREZOID_API_LOGIN and COREZOID_API_SECRET"**
- Проверьте, что `env` в конфиге задан верно и ключи не в кавычках внутри значений.

**Путь с пробелами (Windows)**
- Используйте двойные обратные слэши: `"C:\\Users\\Name\\corezoid-skill\\mcp-server"`
