# Canonical Schemas (Source of Truth)

This document is the **single source of truth** for domain object schemas. Any other schema references must defer to this file.

## Versioning
- `schema_version` is required for all persisted payloads.
- Backwards-compatible changes increment `minor`.
- Breaking changes increment `major` and must be ratified in `research/specs/CONSTITUTION.md`.

## 1. Task
```json
{
  "schema_version": "1.0",
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

## 2. Result
```json
{
  "schema_version": "1.0",
  "task_id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "worker_id": "agent-id",
  "content": "text or url",
  "artifacts": ["path/to/file"],
  "metadata": {
    "execution_time_ms": 120,
    "tool_calls": ["search_tool"]
  },
  "state_version": 1
}
```

## 3. Evaluation
```json
{
  "schema_version": "1.0",
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

## Notes
- `priority` is an integer 1-5 inclusive.
- `metadata` is the canonical key name (not `meta_data`).
- `state_version` is an integer, used for optimistic concurrency control.
