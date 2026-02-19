# Corezoid API Reference (для MCP)

Справочник формата ops для инструмента `corezoid_api_request`. Источник: [corezoid/documentation](https://github.com/corezoid/documentation).

## Аутентификация

MCP использует `COREZOID_API_LOGIN`, `COREZOID_API_SECRET`, `COREZOID_API_BASE_URL`. Подпись: `hex(SHA1(timestamp + secret + content + secret))`.

---

## Создание процесса

**API v1** (задай `COREZOID_API_VERSION=1`; без папки):
```json
{
  "ops": [{
    "type": "create",
    "obj": "conv",
    "title": "My process",
    "description": "Description",
    "status": "active"
  }]
}
```

**API v2** (с папкой) — per swagger: status enum `active` | `paused` | `debug` | `blocked`:
```json
{
  "ops": [{
    "type": "create",
    "obj": "conv",
    "title": "Process name",
    "description": null,
    "folder_id": 11456,
    "company_id": "i7856235891",
    "conv_type": "process",
    "create_mode": "without_nodes",
    "status": "active"
  }]
}
```
Ответ: `obj_id` — ID процесса (conv_id).

---

## Создание папки

Per swagger (create-request-12): `folder_id` = Parent folder ID. При создании внутри stage нужны `stage_id` или `stage_short_name` (и при необходимости `project_id`).

**В корне** (`folder_id: 0` = Root):
```json
{
  "ops": [{
    "type": "create",
    "obj": "folder",
    "title": "My folder",
    "folder_id": 0,
    "company_id": "i7856235891"
  }]
}
```

**Внутри родительской папки** (вне Project/Stage):
```json
{
  "ops": [{
    "type": "create",
    "obj": "folder",
    "title": "Subfolder",
    "folder_id": 2517,
    "company_id": "i7856235891"
  }]
}
```

**Внутри папки в Stage:** если родитель в stage, добавь `stage_id` (или `stage_short_name`) и при необходимости `project_id`:
```json
{
  "ops": [{
    "type": "create",
    "obj": "folder",
    "title": "Subfolder",
    "folder_id": 2517,
    "stage_id": 58,
    "project_id": 123,
    "company_id": "i7856235891"
  }]
}
```
Per swagger: "If the object is in a stage, you must additionally send either stage_id or stage_short_name."

**Перемещение папки** (если create не сработал): операция `link` с `obj: "folder"`:
```json
{
  "type": "link",
  "obj": "folder",
  "obj_id": 2520,
  "obj_type": "folder",
  "folder_id": 2517,
  "parent_id": 0
}
```
`obj_id` — ID перемещаемой папки, `folder_id` — целевая папка, `parent_id` — текущая родительская (0 = Root).

---

## Редактирование процесса

**Название:**
```json
{"type": "modify", "obj": "conv", "obj_id": "1234", "title": "New name"}
```

**Статус** (active | paused | debug | blocked):
```json
{"type": "modify", "obj": "conv", "obj_id": "1234", "status": "active"}
```

**Удаление** (в корзину):
```json
{"type": "delete", "obj": "conv", "obj_id": "1234"}
```

---

## Ноды

**Создание нод** (per swagger: type, obj, conv_id, version, obj_type required; obj_type: 0=normal, 1=start, 2=final, 3=escalation):
```json
{
  "ops": [{
    "type": "create",
    "obj": "node",
    "conv_id": 1234,
    "version": 1662369848,
    "obj_type": 1,
    "title": "Start",
    "description": ""
  }, {
    "type": "create",
    "obj": "node",
    "conv_id": 1234,
    "version": 1662369848,
    "obj_type": 2,
    "title": "Success",
    "description": ""
  }]
}
```
Версию процесса (`version`) получай из `corezoid_list_process_nodes` (commits.version или change_time) или `corezoid_get_process_version`.

**Список нод процесса** (структура процесса с нодами и логикой):
```json
{"type": "list", "obj": "conv", "obj_id": "1234"}
```
Используйте `corezoid_list_process_nodes` — это основной способ получить структуру процесса через API.

**Редактирование логики ноды** (logics — массив правил):
```json
{
  "type": "modify",
  "obj": "node",
  "obj_id": "n10221",
  "conv_id": "1234",
  "logics": [
    {"type": "go", "to_node_id": "n10222"}
  ]
}
```

**Выравнивание нод (position)** — после создания задай координаты через modify:
```json
{
  "type": "modify",
  "obj": "node",
  "obj_id": "n10221",
  "conv_id": "1234",
  "position": [200, 100]
}
```
Для v2 может потребоваться `extra: {"modeForm":"expand","icon":""}` и `version` (unixtime).

`position: [x, y]` — координаты левого верхнего угла ноды. Рекомендуемая сетка: шаг 250–300 px по X и Y.

**Схема выравнивания (слева направо, сверху вниз):**
| Нода | position |
|------|----------|
| Start | [0, 0] |
| Обработка 1 | [300, 0] |
| Обработка 2 | [600, 0] |
| Success | [300, 250] |
| Error | [300, 500] |

**Удаление ноды:**
```json
{"type": "delete", "obj": "node", "obj_id": "n10221", "conv_id": "1234"}
```

---

## Задачи (Tasks)

Используйте готовые инструменты MCP: `corezoid_create_task`, `corezoid_modify_task`, `corezoid_delete_task`.

**Или через corezoid_api_request:**
```json
{
  "ops": [{
    "type": "create",
    "conv_id": 1234,
    "obj": "task",
    "ref": "unique-ref-123",
    "data": {"key": "value"}
  }]
}
```

---

## Версия API

MCP по умолчанию использует **API v2** (`/api/2/json/...`) — рекомендуется для избежания "convert to new format". Задайте `COREZOID_API_VERSION=1` в env MCP для v1. v1: create conv без folder_id; v2: folder_id, company_id, create_mode, conv_type.

---

## Ошибки "Convert to new format" и "Unconfirmed previous version"

**Причина:** API v1 создаёт процессы в старом формате. Corezoid UI требует новый формат.

**Решение:**
1. **Используйте API v2** — задайте `COREZOID_API_VERSION=2` в env MCP.
2. **Создавайте процесс через `corezoid_create_process`** — использует v2 с `create_mode: "without_nodes"`.
3. **Или создайте процесс в UI** — в Corezoid: New Process → сохраните пустой процесс → добавляйте ноды через API.
4. **Deploy в UI** — после изменений через API откройте процесс в Corezoid и нажмите Deploy (если есть незадеплоенные изменения).

**Порядок создания нод (важно):**
1. Создать процесс (v2).
2. Добавить ноды по одной, сохранять `obj_id` из ответа.
3. Сразу задать `position` для каждой ноды (modify).
4. Связать ноды через `logics` (modify).
5. Не менять порядок: create → position → logics.

**Если "unconfirmed previous version":** В UI откройте процесс → Deploy или Confirm. API не имеет отдельной операции deploy для процессов в "My Corezoid".

---

## Если API возвращает ошибку

- **company_id** — для процессов в workspace компании может требоваться `company_id` (формат `i123456789`). Укажите в `corezoid_list_process_nodes(conv_id, company_id="i...")`.
- **Права API-ключа** — в Corezoid: Users & Groups → API Keys → ключ должен иметь доступ к процессу/папке.
- **conv_id** — число из URL процесса или из Start-ноды в Edit mode.

## Типичный workflow

1. **Создать процесс** — `corezoid_create_process` или `corezoid_api_request` с `obj: "conv"`, `title`, `status: "active"`.
2. **Получить версию** — `corezoid_get_process_version(conv_id)` для version.
3. **Добавить ноды** — `corezoid_create_node` или `corezoid_api_request` с `obj: "node"`, `conv_id`, `version`, `obj_type`. Сохрани `obj_id` из ответа.
4. **Выровнять ноды** — `corezoid_modify_node` с `position: [x, y]`, `logics` (текущие или []). Сетка: Start [0,0], шаг 250–300 px.
5. **Связать ноды** — `corezoid_modify_node` с `logics: [{"type":"go","to_node_id":"..."}]`.
6. **Тестировать** — `corezoid_create_task`.
