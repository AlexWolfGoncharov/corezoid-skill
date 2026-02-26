# Corezoid Documentation — Agent Navigation

Use this index to quickly find relevant sections. Do not load the entire
`Corezoid-documentation.md`; open only required chunks from `references/docs/`.

---

## Quick Topic Lookup

| Topic | File | Notes |
|------|------|-------|
| Platform introduction and overview | `01-introduction.md` | — |
| UI interface (Workspace, Monitor, Users & Groups, Editor) | `02-interface.md` | — |
| Core concepts (Nodes, Tasks, Processes, Parameters, Functions) | `03-core-concepts.md` | — |
| Node notation and parameter semantics | `03-core-concepts.md` § 2.3.9 | — |
| Nodes: Start, End, Condition, Delay | `04-nodes-flow.md` | — |
| Nodes: Set Parameters, Code | `05-nodes-set-code.md` | — |
| Node: Git Call | `06-nodes-git-call.md` | — |
| Nodes: API Call, Database Call | `07-nodes-api-db.md` | — |
| Nodes: Queue, Get from Queue, Copy, Call, Reply | `08-nodes-queue-copy-call.md` | — |
| Nodes: Set State, Callback, Modify Task, Sum | `09-nodes-callback-modify-sum.md` | — |
| Deployment (VMware, virtualization) | `10-deployment.md` | — |
| Process guide and advanced features | `11-processes-advanced.md` | — |
| Communications Orchestrator | `12-communications-orchestrator.md` | — |
| Tutorials | `13-tutorials.md` | — |
| References (API, errors, security, SDK) | `14-references.md` | — |

---

## Node Map

| Node | File | When to use |
|------|------|-------------|
| Start | `04-nodes-flow.md` | Webhook/direct URL/process ID/API key behavior |
| End | `04-nodes-flow.md` | Success/error finals, counters, archive/export |
| Condition | `04-nodes-flow.md` | Conditional routing (`go_if_const`, branches) |
| Delay | `04-nodes-flow.md` | Deferred routing and timing controls |
| Set Parameters | `05-nodes-set-code.md` | Add/update task parameters |
| Code | `05-nodes-set-code.md` | JavaScript/Erlang data logic |
| Git Call | `06-nodes-git-call.md` | Execute external repository logic |
| API Call | `07-nodes-api-db.md` | HTTP integrations |
| Database Call | `07-nodes-api-db.md` | SQL/database integrations |
| Queue | `08-nodes-queue-copy-call.md` | Queue buffering and load control |
| Get from Queue | `08-nodes-queue-copy-call.md` | Retrieve queued tasks |
| Copy Task | `08-nodes-queue-copy-call.md` | `api_copy`, fire-and-forget |
| Call a Process | `08-nodes-queue-copy-call.md` | `api_rpc`, wait for reply |
| Reply to Process | `08-nodes-queue-copy-call.md` | Return data to caller process |
| Set State | `09-nodes-callback-modify-sum.md` | State Diagram transitions |
| Waiting for Callback | `09-nodes-callback-modify-sum.md` | External callback wait |
| Modify Task | `09-nodes-callback-modify-sum.md` | Update tasks by reference |
| Sum | `09-nodes-callback-modify-sum.md` | Numeric aggregation logic |

---

## Parameters and REF

| Topic | File |
|------|------|
| REF uniqueness rules | `03-core-concepts.md` § 2.3.2 |
| Input/Local/Output task parameters | `03-core-concepts.md` § 2.3.2.2 |
| Global/system parameters | `03-core-concepts.md` § 2.3.5 |
| `{{conv[...].ref[...]}}` state access pattern | `03-core-concepts.md` § 2.3.5 |
| `{{node[...].count}}`, `{{node[...].SumID}}` | `03-core-concepts.md` § 2.3.5 |
| Built-in functions (`$.math()`, `$.random()`, `$.sha1_hex()`) | `03-core-concepts.md` § 2.3.6 |

---

## API and Integration

| Topic | File |
|------|------|
| API reference, auth, ops format | `14-references.md` § 12.3 |
| Create/modify/delete task examples | `14-references.md` § 12.3 |
| Folder creation in stage context | `references/Corezoid-API-reference.md` |
| Error codes and troubleshooting | `14-references.md` § 12.4 |
| Corezoid SDK references | `14-references.md` § 12.11 |

---

## Playbooks, Templates, Samples, Schema

| Need | Path | Use when |
|------|------|----------|
| Step-by-step implementation strategy | `references/playbooks/` | New workflow needs predictable build steps |
| Fast bootstrap process skeleton | `references/templates/` | Building from scratch is unnecessary |
| Proven implementation examples | `references/samples/` | You need real payload or branch examples |
| Strict JSON structure validation | `references/json-schema/` | Final validation before handoff/deploy |

Recommended path for new implementation:
1. Start from `references/templates/`.
2. Follow `references/playbooks/`.
3. Compare edge logic with `references/samples/`.
4. Validate structure with `references/json-schema/`.

---

## Suggested Reading Order

1. New to platform: `01-introduction.md` -> `03-core-concepts.md`
2. Process building: `03-core-concepts.md` -> `04-nodes-flow.md`
3. Data operations: `05-nodes-set-code.md`, `07-nodes-api-db.md`
4. Inter-process patterns: `08-nodes-queue-copy-call.md`
5. API automation: `14-references.md` + `references/Corezoid-API-reference.md`

---

## File Layout

```
references/
├── INDEX.md
├── Corezoid-API-reference.md
├── Corezoid-swagger-map.md
├── Corezoid-documentation.md
├── playbooks/
├── templates/
├── samples/
├── json-schema/
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
