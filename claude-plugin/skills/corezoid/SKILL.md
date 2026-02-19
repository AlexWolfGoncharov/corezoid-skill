---
name: corezoid
description: Use when the task involves Corezoid: processes, state diagrams, nodes (Start, End, Condition, API Call, Code, Git Call, Queue, etc.), tasks, parameters, dashboards, deployment, API, or Communications Orchestrator. Use when the user asks about Corezoid documentation, workflows, or integration.
---

# Corezoid

Skill for working with the Corezoid platform: cloud actor engine, processes, nodes, tasks, and API.

## Reference

**Документация:**
- **[references/Corezoid-documentation.md](references/Corezoid-documentation.md)** — полная документация (концепты, ноды, UI, deployment). Ищи по номеру раздела (2.3.2, 3.8) или ключевому слову.
- **[references/Corezoid-API-reference.md](references/Corezoid-API-reference.md)** — формат ops для API. **Читай перед использованием `corezoid_api_request`** для создания процессов, папок, нод, редактирования.

**Когда что загружать:**
- Концепты, ноды, параметры, REF → Corezoid-documentation.md
- Создание/редактирование процесса, папки, нод через API → Corezoid-API-reference.md

## Quick orientation

- **Process** = sequence of nodes; **Task** = JSON key-value data unit; **Node** = step (Start, End, Condition, Code, API Call, etc.).
- **REF** = unique task reference in a process. Required for tasks not in final nodes.
- Task parameters: Input, Local, Output. Global params: `root.ref`, `root.node_id`, `root.conv_id`, etc.
- State Diagram: get data with `{{conv[Process_ID].ref[REF]}}` or `{{conv[Process_ID].ref[REF].parameter}}`.

## MCP Tools

Инструменты приходят из MCP Corezoid. Имя сервера может быть любым: `corezoid`, `mcp-corezoid`, `mcp-corezoid-ma`, `mcp-corezoid-az` и т.д. — используй доступные инструменты Corezoid.

**Инструменты:** `corezoid_create_process`, `corezoid_create_task`, `corezoid_modify_task`, `corezoid_delete_task`, `corezoid_list_process_nodes`, `corezoid_get_process`, `corezoid_api_request`, `corezoid_batch_tasks`.

**Перед вызовом** прочитай [Corezoid-API-reference.md](references/Corezoid-API-reference.md) — там формат ops.

### Инструменты

| Инструмент | Задача |
|------------|--------|
| `corezoid_create_process` | Создать процесс (v2, избегает "convert to new format") |
| `corezoid_create_task` | Создать задачу в процессе |
| `corezoid_modify_task` | Изменить задачу по REF |
| `corezoid_delete_task` | Удалить задачу по obj_id |
| `corezoid_list_process_nodes` | Получить структуру процесса (ноды, логика) |
| `corezoid_api_request` | Любые операции API (folder, node, bulk) |

### Workflow: создать процесс и протестировать

1. **Создать процесс** — `corezoid_create_process` (v2 по умолчанию) или `corezoid_api_request`. v2 избегает "convert to new format".
2. **Добавить ноды** — `corezoid_api_request` с `obj: "node"`, `conv_id`, `obj_type`. Сохрани `obj_id` из ответа.
3. **Выровнять ноды** — для каждой ноды: `corezoid_api_request` с `type: "modify"`, `obj: "node"`, `obj_id`, `conv_id`, `position: [x, y]`. Сетка: Start [0,0], шаг 250–300 px. Без этого ноды будут наложены.
4. **Связать ноды** — `corezoid_api_request` с `type: "modify"`, `obj: "node"`, `logics: [{type:"go", to_node_id:"..."}]`.
5. **Тестировать** — `corezoid_create_task(conv_id, ref, data)`.

### Переменные окружения

`COREZOID_API_LOGIN`, `COREZOID_API_SECRET`, `COREZOID_API_BASE_URL`, `COREZOID_API_VERSION` (по умолчанию "2"). Задай в настройках плагина или в окружении.

### Если API возвращает ошибку

- **"Convert to new format" / "Unconfirmed previous version"** — используй `corezoid_create_process` (v2), задай `COREZOID_API_VERSION=2`, или создай процесс в UI. См. troubleshooting в Corezoid-API-reference.md.
- **company_id** — для процессов в workspace компании передай `company_id` (формат `i123456789`).
- **Права API-ключа** — ключ должен иметь доступ к процессу (Users & Groups → API Keys).
