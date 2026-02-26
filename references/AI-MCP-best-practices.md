# AI MCP and Skill Best Practices

This note captures practical guidance used to improve this repository.

## MCP Server Best Practices

- Keep tool contracts strict and predictable (clear schemas, explicit errors).
- Return structured responses (`status_code`, parsed JSON, clear error fields).
- Prefer safe defaults and explicit fallbacks (for example, env-based `company_id`).
- Use focused tools with clear names and concise descriptions.
- Validate input early and fail with actionable error messages.

## Skill Authoring Best Practices

- Keep `SKILL.md` concise and operational.
- Separate references from instructions (playbooks/templates/samples/schema).
- Add deterministic workflow and final validation checklist.
- Document edge cases and anti-patterns (for example, Copy vs Call Process confusion).

## Sources

- https://support.anthropic.com/en/articles/11596040-best-practices-for-building-mcp-servers
- https://www.anthropic.com/engineering/writing-tools-for-agents
- https://modelcontextprotocol.io/specification/2025-11-25
- https://modelcontextprotocol.io/docs/concepts/tools
- https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api
- https://developers.openai.com/api/docs/guides/structured-outputs
- https://cursor.com/docs/context/skills
