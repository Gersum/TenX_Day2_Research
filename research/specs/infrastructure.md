# Infrastructure Specifications (Project Chimera)

## 1. Containerization (Docker)
**Objective**: Ensure identical environments for local development and agentic workers.

### 1.1 Dockerfile Strategy
- **Base Image**: `python:3.11-slim`
- **Dependency Manager**: `uv` (installed via official installer).
- **Security**: Non-root user `chimera_user`.
- **Exposed Ports**: 8000 (API), 6379 (Redis - internal).

### 1.2 Multi-Agent Orchestration (Compose)
- `chimera-core`: The main orchestrator/planner.
- `chimera-worker`: Replicable worker containers.
- `chimera-judge`: The validation gatekeeper.
- `redis`: Shared Hot-State storage.

## 2. CI/CD Pipeline (GitHub Actions)
**Objective**: Automate reliability checks.

### 2.1 Quality Gates
1.  **Lint**: `ruff` for fast Python linting.
2.  **Type Check**: `pyright` or `mypy`.
3.  **Test**: `pytest` with 80% coverage threshold.
4.  **Security**: `bandit` or `snyk` stub for vulnerability scanning.

## 3. Reliability Engineering (SRE)
- **Monitoring**: All agents must output structured JSON logs (pydantic-based).
- **Self-Healing**: If a worker container crashes, the Orchestrator must recognize the `PENDING` task in Redis and re-assign.
- **Traceability**: All agentic transitions are logged to the Tenx MCP Sense "Flight Recorder."

## 4. Swarm-Ready Readiness
- Configuration must be 100% environment-variable driven (Twelve-Factor App).
- Explicit `AGENTS.md` (as per Spec Kit) to define the mission boundaries.
