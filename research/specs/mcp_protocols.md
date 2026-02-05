# MCP Protocols Specification

## 1. Core Primitives
- **Resources**: Data payloads (documents, embeddings, research notes).
- **Tools**: Executable actions (search, file operations, commerce).
- **Prompts**: Structured templates for deterministic reasoning.

**Design Principle**: MCP is the "USB-C for AI"  a standardized interface that decouples internal reasoning from external APIs.

## 2. Topology: Host & Servers
- **MCP Host (Agent Runtime)**: The central runtime where Planner/Worker/Judge operate.
- **MCP Servers (Capability Providers)**: Independent services wrapping external APIs.
  - Examples: `mcp-server-twitter`, `mcp-server-weaviate`, `mcp-server-coinbase`.

## 2.1 Transports
- **Stdio**: Local tool execution.
- **SSE/HTTP**: Remote tool execution.

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
- **coinbase_tool**: Execute on-chain actions (via mcp-server-coinbase or equivalent).

## 3.1 Decoupled Action Logic
All financial actions must be executed **only** via MCP tools to keep core reasoning logic separated from blockchain implementation details.

## 3.2 Governance Constraints
- **No Direct API Calls**: All external actions must pass through MCP Tools.
- **Rate Limiting & Logging**: Enforced at MCP Server layer for auditability and safety.

## 4. Resource Model (Perception)
Resources represent passive data streams the agents consume.
- Examples: `news://ethiopia/latest`, `social://mentions`.

### 4.1 Perceptual Polling
- Agents poll configured Resource URIs on a schedule to detect changes.

### 4.2 Abstraction Layer
- Agents bind to **resource URIs**, not vendor APIs, allowing provider swaps without code changes.

### 4.3 Context Injection
- Resource ingestion dynamically assembles context by injecting **SOUL.md** and long-term memory (Weaviate) into the LLM window.

## 5. Swarm Integration
- **Planner** subscribes to resource updates and spawns tasks.
- **Workers** execute MCP Tools for actions (posting, querying, transactions).
- **Context Assembly**: Resources inject SOUL.md + long-term memory (Weaviate) into the LLM context window.

## 6. Tool Safety Extensions
- **Dry-Run Support**: Tools should support a dry-run mode for preflight checks.
- **Rate Limits**: Enforced at the MCP Server layer with consistent logging.

## 7. Prompt Standardization
- Reusable prompts enforce consistent reasoning patterns (e.g., `analyze_sentiment`, `extract_topics`).
- System prompt updates are centrally managed to propagate brand/ethical changes across the fleet.

## 4. Prompt Registry
All prompts are versioned and must reference the governing SOUL and BoardKit policies.
