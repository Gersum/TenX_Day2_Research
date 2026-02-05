# Technical Specification

## API Contracts (JSON)
### Task
```json
{
  "id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "goal_id": "uuid-v4",
  "type": "RESEARCH | CONTENT | REVIEW | ACTION",
  "description": "text",
  "status": "PENDING | ASSIGNED | COMPLETED | FAILED",
  "priority": 1,
  "context": {
    "target_platform": "twitter",
    "constraints": ["max_length: 280"]
  },
  "created_at": "ISO-8601"
}
```

### Result
```json
{
  "task_id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "worker_id": "agent-id",
  "content": "text or url",
  "artifacts": ["path/to/file"],
  "meta_data": {
    "execution_time_ms": 120,
    "tool_calls": ["search_tool"]
  },
  "state_version": 1
}
```

### Evaluation
```json
{
  "task_id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "judge_id": "judge-agent-1",
  "confidence_score": 0.85,
  "verdict": "APPROVE | REJECT | ESCALATE",
  "feedback": "text",
  "state_version": 1,
  "policy_checks": [
    {"rule": "No hate speech", "passed": true}
  ]
}
```

## Database Schema (ERD)
### Entities
- **agents**(id, tenant_id, name, wallet_address, status, created_at)
- **users**(id, tenant_id, tier, api_keys)
- **ledgers**(id, tenant_id, agent_id, amount, currency, tx_hash, timestamp)
- **videos**(id, tenant_id, agent_id, platform, title, url, status, created_at)

### Relationships
- agents 1..* videos
- agents 1..* ledgers
- tenants 1..* agents/users/videos/ledgers
