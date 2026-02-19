# Corezoid MCP & Skills

MCP-коннектор и Skills для работы с Corezoid через AI-агентов (Cursor, Claude Desktop, Codex).

## Содержимое

- **mcp-server/** — MCP-сервер (инструменты для создания/редактирования процессов, нод, задач)
- **claude-plugin/** — плагин для Claude Desktop (MCP + skill)
- **SKILL.md** — skill для Codex/Cursor
- **references/** — документация Corezoid, API reference, swagger map

## Быстрый старт

1. Настрой MCP: см. `mcp-server/README.md` и `mcp-server/CLAUDE-MCP-SETUP.md`
2. Задай переменные: `COREZOID_API_LOGIN`, `COREZOID_API_SECRET`
3. Используй инструменты: `corezoid_create_task`, `corezoid_create_process`, `corezoid_api_request` и др.

## Возможности

- Понимание структуры процессов (ноды, логика, параметры)
- Редактирование существующих процессов и задач
- Создание новых процессов, папок, нод через API
