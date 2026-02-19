# Corezoid Documentation — Навигация для агентов

Используй этот индекс, чтобы быстро найти нужный раздел. Не загружай весь `Corezoid-documentation.md` — открывай только релевантные чанки.

---

## Быстрый поиск по теме

| Тема | Файл | Строки (прим.) |
|------|------|----------------|
| **Введение, обзор платформы** | `01-introduction.md` | — |
| **Интерфейс UI** (Workspace, Activity Monitor, Users & Groups, Process Editor) | `02-interface.md` | — |
| **Базовые концепции** (Nodes, Tasks, Processes, Parameters, Functions, Dashboards, Projects) | `03-core-concepts.md` | — |
| **Схема нотации** параметров нод | `03-core-concepts.md` § 2.3.9 | — |
| **Ноды: Start, End, Condition, Delay** | `04-nodes-flow.md` | — |
| **Ноды: Set Parameters, Code** | `05-nodes-set-code.md` | — |
| **Нода: Git Call** | `06-nodes-git-call.md` | — |
| **Ноды: API Call, Database Call** | `07-nodes-api-db.md` | — |
| **Ноды: Queue, Get from Queue, Copy Task, Call a Process, Reply to Process** | `08-nodes-queue-copy-call.md` | — |
| **Ноды: Set State, Waiting for Callback, Modify Task, Sum** | `09-nodes-callback-modify-sum.md` | — |
| **Deployment** (VMware, virtualization) | `10-deployment.md` | — |
| **Processes Guide, Advanced Features** | `11-processes-advanced.md` | — |
| **Communications Orchestrator** (боты в мессенджерах) | `12-communications-orchestrator.md` | — |
| **Tutorials** | `13-tutorials.md` | — |
| **References** (Definitions, API, Error Codes, Security, SDK) | `14-references.md` | — |

---

## Детальная карта по нодам

| Нода | Файл | Когда смотреть |
|------|------|----------------|
| Start | `04-nodes-flow.md` | Webhook, Direct URL, Process ID, API key |
| End | `04-nodes-flow.md` | Success/Error, счётчики, экспорт задач |
| Condition | `04-nodes-flow.md` | Условия, маршрутизация, go_if_const |
| Delay | `04-nodes-flow.md` | Пауза, semaphors, отложенные задачи |
| Set Parameters | `05-nodes-set-code.md` | Добавление/изменение параметров задачи |
| Code | `05-nodes-set-code.md` | JavaScript/Erlang, data manipulation |
| Git Call | `06-nodes-git-call.md` | Код из Git, Docker, JSON-RPC |
| API Call | `07-nodes-api-db.md` | HTTP-запросы, внешние API |
| Database Call | `07-nodes-api-db.md` | SQL, подключение к БД |
| Queue | `08-nodes-queue-copy-call.md` | Очередь задач, load balancing |
| Get from Queue | `08-nodes-queue-copy-call.md` | Получение задач из очереди |
| Copy Task | `08-nodes-queue-copy-call.md` | Копирование задачи в другой процесс (api_copy, mode create). НЕ ждёт ответа. |
| Call a Process | `08-nodes-queue-copy-call.md` | Вызов процесса как функции (api_rpc). Ждёт Reply to Process. НЕ путать с Copy Task. |
| Reply to Process | `08-nodes-queue-copy-call.md` | Ответ в вызывающий процесс |
| Set State | `09-nodes-callback-modify-sum.md` | State Diagram, смена состояния |
| Waiting for Callback | `09-nodes-callback-modify-sum.md` | Ожидание callback, webhook |
| Modify Task | `09-nodes-callback-modify-sum.md` | Изменение параметров задачи |
| Sum | `09-nodes-callback-modify-sum.md` | Суммирование параметров |

---

## Параметры и REF

| Тема | Файл |
|------|------|
| REF (уникальность в процессе) | `03-core-concepts.md` § 2.3.2 |
| Task parameters (Input, Local, Output) | `03-core-concepts.md` § 2.3.2.2 |
| Global parameters | `03-core-concepts.md` § 2.3.5 |
| `{{conv[...].ref[...]}}` — доступ к State Diagram | `03-core-concepts.md` § 2.3.5 |
| `{{node[...].count}}`, `{{node[...].SumID}}` | `03-core-concepts.md` § 2.3.5 |
| Функции `$.math()`, `$.random()`, `$.sha1_hex()` | `03-core-concepts.md` § 2.3.6 |

---

## API и интеграция

| Тема | Файл |
|------|------|
| API Reference, authentication, ops format | `14-references.md` § 12.3 |
| Create/Modify/Delete task примеры | `14-references.md` § 12.3 |
| **Folders** (создание внутри папки, stage_id, link для перемещения) | `references/Corezoid-API-reference.md` § Создание папки |
| Error codes, troubleshooting | `14-references.md` § 12.4 |
| Corezoid SDK (PHP, Java, Python, etc.) | `14-references.md` § 12.11 |

---

## Рекомендуемый порядок чтения

1. **Новичок:** `01-introduction.md` → `03-core-concepts.md` (Nodes, Tasks, Processes)
2. **Создание процесса:** `03-core-concepts.md` → `04-nodes-flow.md` (Start, End, Condition)
3. **Работа с данными:** `05-nodes-set-code.md`, `07-nodes-api-db.md`
4. **Межпроцессное взаимодействие:** `08-nodes-queue-copy-call.md`
5. **API/автоматизация:** `14-references.md` + `references/Corezoid-API-reference.md`

---

## Расположение файлов

```
references/
├── INDEX.md                    ← этот файл (навигация)
├── Corezoid-API-reference.md   ← формат ops для MCP/API
├── Corezoid-documentation.md   ← полная документация (оригинал, ~10k строк)
└── docs/
    ├── 01-introduction.md
    ├── 02-interface.md
    ├── 03-core-concepts.md
    ├── 04-nodes-flow.md
    ├── 05-nodes-set-code.md
    ├── 06-nodes-git-call.md
    ├── 07-nodes-api-db.md
    ├── 08-nodes-queue-copy-call.md
    ├── 09-nodes-callback-modify-sum.md
    ├── 10-deployment.md
    ├── 11-processes-advanced.md
    ├── 12-communications-orchestrator.md
    ├── 13-tutorials.md
    └── 14-references.md
```
