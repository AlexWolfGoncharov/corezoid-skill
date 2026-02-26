# Corezoid Swagger Ops Map

Generated from `swagger.json` on 2026-02-18 (UTC).

## API Shape

- OpenAPI: `3.0.1`
- API title: `Corezoid API`
- API version: `2.0`
- Default server: `https://api.corezoid.com/`
- Total paths: `70`
- Core request envelope for JSON operations: `{"ops": [ { ...operation... } ]}`

## Authentication (from Swagger)

- `apiKey`: type `apiKey`
  - credential placeholder in path: `{API_LOGIN}/{GMT_UNIXTIME}/{SIGNATURE}`
  - location: `path`

## Core Ops By Tag

Use this section when composing `ops` for `corezoid_api_request`.

### `conv`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_21}/{SIGNATURE}` (`operationId`: `conv`)
  - supported `type` values and key required fields:
    - `create`: `type, obj`
    - `modify`: `type, obj, obj_id`
    - `list`: `type, obj, obj_id`
    - `show`: `type, obj, obj_id`
    - `link`: `type, obj, obj_id, obj_to, privs`
    - `favorite`: `type, obj, obj_id, favorite`
    - `delete`: `type, obj, obj_id`
    - `restore`: `type, obj, obj_id`
    - `destroy`: `type, obj, obj_id`

### `convs`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_22}/{SIGNATURE}` (`operationId`: `convs`)
  - supported `type` values and key required fields:
    - `list`: `type, obj`

### `node`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_37}/{SIGNATURE}` (`operationId`: `node`)
  - supported `type` values and key required fields:
    - `create`: `type, obj, conv_id, version, obj_type`
    - `modify`: `type, obj, conv_id, obj_type, obj_id, logics`
    - `list`: `type, obj, conv_id, obj_id, limit`
    - `show`: `type, obj, conv_id, obj_id`
    - `delete`: `type, obj, conv_id, obj_id`
    - `reset`: `type, obj, conv_id, obj_id`

### `nodes`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_38}/{SIGNATURE}` (`operationId`: `nodes`)
  - supported `type` values and key required fields:
    - `list`: `type, obj, pattern`

### `task`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_56}/{SIGNATURE}` (`operationId`: `task`)
  - supported `type` values and key required fields:
    - `create`: `type, obj, conv_id, data`
    - `modify`: `type, obj, conv_id, data`
    - `show`: `type, obj, conv_id, ref, obj_id`
    - `delete`: `type, obj, conv_id, node_id, obj_id`
    - `step_next`: `type, obj, conv_id, data, obj_id`
    - `step_prev`: `type, obj, conv_id, data, obj_id`
    - `step_goto`: `type, obj, conv_id, data, obj_id`

### `folder`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_27}/{SIGNATURE}` (`operationId`: `folder`)
  - supported `type` values and key required fields:
    - `create`: `type, obj`
    - `modify`: `type, obj, obj_id`
    - `link`: `type, obj, obj_id, obj_to, obj_type`
    - `list`: `type, obj, obj_id`
    - `show`: `type, obj, obj_id`
    - `favorite`: `type, obj, obj_id, favorite`
    - `delete`: `type, obj, obj_id`
    - `destroy`: `type, obj, obj_id`
    - `restore`: `type, obj, obj_id`

### `commit`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_11}/{SIGNATURE}` (`operationId`: `commit`)
  - supported `type` values and key required fields:
    - `confirm`: `type, obj, version, conv_id`
    - `show`: `type, obj, version, conv_id`
    - `delete`: `type, obj, version, obj_id, obj_type`

### `commits`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_12}/{SIGNATURE}` (`operationId`: `commits`)
  - supported `type` values and key required fields:
    - `list`: `type, obj, conv_id`

### `company`

- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_15}/{SIGNATURE}` (`operationId`: `company`)
  - supported `type` values and key required fields:
    - `create`: `type, obj, site, name, description`
    - `list`: `type, obj`
- `POST /api/2/json/{API_LOGIN}/{GMT_UNIXTIME_16}/{SIGNATURE}` (`operationId`: `companyMultitenant`)
  - supported `type` values and key required fields:
    - `create`: `type, obj, login, login_type`
    - `modify`: `type, obj, company_id, auth_providers`
    - `list`: `type, obj`
    - `delete`: `type, obj, obj_id`

## Swagger-Driven Guardrails

- Keep `obj` aligned with tag intent (`conv`, `node`, `task`, `folder`).
- For process/node/task mutations, always include all required fields from the mapped schema.
- Prefer declared `type` values from the discriminator mapping; avoid guessing unsupported `type` names.
- If tool wrappers differ from Swagger enums (for example process status naming), verify with current workspace behavior before bulk changes.
