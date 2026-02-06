# Data Model: Project Chimera Core System

## Overview
Defined entities and schema references for the core Chimera system.

## Entities

### `Task`
Atomic unit of work distributed to agents.
- **Source**: `research/specs/core_interfaces.md` (Section 1.1)
- **Key Fields**: `id`, `tenant_id`, `type`, `status`
- **Validation**:
  - `priority` must be 1-5.
  - `tenant_id` is mandatory for isolation.

### `Result`
Output artifact from a Worker execution.
- **Source**: `research/specs/core_interfaces.md` (Section 1.2)
- **Key Fields**: `task_id`, `content`, `artifacts`
- **Validation**:
  - `worker_id` must match a valid agent.

### `Evaluation`
Quality and policy check result from a Judge.
- **Source**: `research/specs/core_interfaces.md` (Section 1.3)
- **Key Fields**: `verdict`, `confidence_score`
- **Validation**:
  - `verdict` in [APPROVE, REJECT, ESCALATE].

### `Agent`
System representation of an acting entity.
- **Source**: `research/specs/data_models.md` (PostgreSQL Schema)
- **Key Fields**: `id`, `tenant_id`, `role` (Planner/Worker/Judge)

## Storage Strategy
- **Relational (Postgres)**: `Agents`, `Users`, `Ledgers` (Audit trail).
- **Key-Value (Redis)**: Task Queues (`queue:task`), Agent State.
- **Vector (Weaviate)**: Semantic Memory (`Memory` class).

## Schema Definitions
See `contracts/` for precise JSON Schemas.
