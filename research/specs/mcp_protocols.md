# MCP Protocols Specification

## 1. Core Primitives
- **Resources**: Data payloads (documents, embeddings, research notes).
- **Tools**: Executable actions (search, file operations, commerce).
- **Prompts**: Structured templates for deterministic reasoning.

## 2. Standard Resource Schemas
### proposal/v1
```json
{
  "id": "uuid-v4",
  "from_agent": "agent-id",
  "to_agent": "agent-id",
  "topic": "collaboration-topic",
  "value_exchange": "bounty | barter | none",
  "constraints": ["deadline: ISO-8601"],
  "created_at": "ISO-8601"
}
```

### review/v1
```json
{
  "id": "uuid-v4",
  "task_id": "uuid-v4",
  "reviewer_id": "agent-id",
  "score": 0.0,
  "verdict": "APPROVE | REJECT",
  "notes": "text",
  "created_at": "ISO-8601"
}
```

## 3. Tool Registry
Each agent must expose an MCP registry of available tools.
- **search_tool**: Query web sources.
- **filesystem_tool**: Read/write project artifacts.
- **commerce_tool**: Perform budget-checked transactions.

## 4. Prompt Registry
All prompts are versioned and must reference the governing SOUL and BoardKit policies.
