# Orchestration Specification

## 1. Fractal Orchestration Pattern
To prevent human cognitive overload, the system uses a **tiered management hierarchy**:

- **Super-Orchestrator (Human)**
  - Defines high-level strategy, budgets, and constraints.
- **Manager Agents**
  - Translate strategy into campaigns and objectives.
- **Worker Swarms**
  - Execute atomic tasks in parallel.

## 2. FastRender Swarm Roles
- **Planner (Strategist)**: Decomposes goals into atomic tasks.
- **Worker (Executor)**: Executes tasks using MCP tools.
- **Judge (Gatekeeper)**: Approves/rejects output for quality, safety, alignment.

## 3. Workflow State Machine
```
Goal -> Plan -> Queue(Task) -> Execute -> Review -> (Approve | Reject | Escalate)
```

## 4. Retry  Self-Healing
- **Retry Rule**: A failed task is re-queued once.
- **Escalation Rule**: After 2 failed attempts, send to Judge for triage.
- **Management by Exception**: Only escalated tasks reach human review.

## 5. Observability
- Every transition emits an event log entry.
- Swarm traces are recorded via MCP Sense for audit.
