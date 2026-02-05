# Data Models & Storage Schema

## Overview
Definition of the Hybrid Data Architecture (SQL + NoSQL + Vector).

## 1. PostgreSQL Schema (System of Record)
**Objective**: Transactional consistency for core entities.

### Tables
- `agents`: (id, tenant_id, name, wallet_address, config_json)
- `users`: (id, tenant_id, tier, api_keys)
- `ledgers`: (id, tenant_id, agent_id, amount, currency, tx_hash, timestamp)

```sql
CREATE TABLE agents (
    id UUID PRIMARY KEY,
  tenant_id UUID NOT NULL,
    name VARCHAR(255),
    wallet_address VARCHAR(42),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 2. Redis Schema (Hot State)
**Objective**: Sub-millisecond queuing and ephemeral interaction state.

### Keys
- `queue:task`: List of JSON Strings (Task Objects).
- `queue:review`: List of JSON Strings (Result Objects).
- `agent:{id}:state`: Hash map of current context (last_seen, current_task).
- `agent:{id}:episodic`: Short-term memory cache for immediate context.

## 3. Weaviate Schema (Semantic Memory)
**Objective**: RAG for persona and research.

### Classes
- `Memory`:
  - `content`: Text (The memory).
  - `agent_id`: String (Owner).
  - `type`: String ("episodic", "semantic").
  - `embedding`: Vector[1536].

```graphql
class Memory {
    content: text
    agent_id: string
    timestamp: date
}
```
