# Orchestration Specification

## 1. Fractal Orchestration Pattern
To prevent human cognitive overload, the system uses a **tiered management hierarchy** designed for a **single operator or small team** to manage a massive fleet:

- **Super-Orchestrator (Human)**
  - Defines high-level strategy, budgets, and constraints.
- **Manager Agents**
  - Translate strategy into campaigns and objectives.
- **Worker Swarms**
  - Execute atomic tasks in parallel.

**Scale Target**: The architecture must support **1,000+ concurrent agents** via container orchestration (see infrastructure spec).

## 2. FastRender Swarm Roles
- **Planner (Strategist)**: Decomposes goals into atomic tasks and **task graphs (DAGs)** with explicit dependencies.
- **Worker (Executor)**: Executes tasks using MCP tools in a **shared-nothing** model to prevent cascading failures.
- **Judge (Gatekeeper)**: Approves/rejects output for quality, safety, alignment.
- **Triage Agent (Resilience)**: Detects routine failures (timeouts, tool errors) and applies automated recovery steps before escalation.
- **CFO Judge (Financial)**: Reviews and approves all financial actions before execution.

**Control Plane**: Manager Agents direct multiple FastRender swarms (Planner/Worker/Judge) and apply BoardKit policies to enforce global brand and ethical alignment.

## 3. Workflow State Machine
```
Goal -> Plan -> Queue(Task) -> Execute -> Review -> (Approve | Reject | Escalate)
```

## 4. Retry & Self-Healing
- **Retry Rule**: A failed task is re-queued once.
- **Escalation Rule**: After 2 failed attempts, send to Judge for triage.
- **Triage Rule**: Triage Agents attempt automated recovery for routine errors (API timeouts, rate limits, partial outputs).
- **Management by Exception**: Only escalated tasks reach human review.

## 5. Observability
- Every transition emits an event log entry.
- Swarm traces are recorded via MCP Sense for audit.
