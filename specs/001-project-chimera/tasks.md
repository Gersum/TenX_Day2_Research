# Tasks: Project Chimera Core System

## Dependencies
- US1 (Planner) depends on Foundational (Models)
- US2 (Worker) depends on US1
- US3 (Judge) depends on US2
- US4 (CFO) depends on US3
- US5 (Orchestrator) depends on US1-US4
- US6 (Tenant Isolation) is Foundational

## Phase 1: Setup
- [x] T001 Initialize Python library structure `src/chimera_core` (Library-First Principle)
- [x] T002 Configure `pyproject.toml` with dependencies (pydantic, redis, etc.)
- [x] T003 Create `tests/fixtures/` and `tests/conftest.py`
- [x] T004 Define JSON Schemas for `Task`, `Result`, `Evaluation` in `contracts/`

## Phase 2: Foundational (Blocking)
- [x] T005 [US6] Write failing tests for `TenantContext` isolation logic in `tests/core/test_security.py`
- [ ] T006 [US6] Implement `TenantContext` middleware using `X-Tenant-ID` header in `src/chimera_core/security.py`
- [ ] T007 [P] [US1] Write failing tests for Pydantic Models in `tests/core/test_models.py`
- [ ] T008 [P] [US1] Implement Pydantic models validating against `contracts/` in `src/chimera_core/models.py`

## Phase 3: User Story 1 (Planner)
- [ ] T009 [US1] Write failing contract tests for `PlannerAgent` interface in `tests/agents/test_planner.py`
- [ ] T010 [US1] Implement `BaseAgent` abstract class in `src/chimera_core/agents/base.py`
- [ ] T011 [US1] Implement `PlannerAgent` with decomposition logic (mocked LLM) in `src/chimera_core/agents/planner.py`

## Phase 4: User Story 2 (Worker)
- [ ] T012 [US2] Write failing tests for `WorkerAgent` tool usage in `tests/agents/test_worker.py`
- [ ] T013 [US2] Implement `MCPClient` wrapper in `src/chimera_core/mcp/client.py` (Audit logging)
- [ ] T014 [US2] Implement `WorkerAgent` executing tasks via MCP in `src/chimera_core/agents/worker.py`

## Phase 5: User Story 3 & 4 (Governance)
- [ ] T015 [P] [US3] Write failing tests for `JudgeAgent` validation logic in `tests/agents/test_judge.py`
- [ ] T016 [P] [US4] Write failing tests for `BudgetGuard` logic in `tests/governance/test_budget.py`
- [ ] T017 [P] [US3] Implement `JudgeAgent` with policy checks in `src/chimera_core/agents/judge.py`
- [ ] T018 [P] [US4] Implement `BudgetGuard` transaction gating in `src/chimera_core/governance.py`

## Phase 6: Orchestration
- [ ] T019 [US5] Implement `Orchestrator` entry point in `src/chimera_core/orchestrator.py`
- [ ] T020 [P] [US5] Create simple CLI dashboard in `src/chimera_core/cli.py`

## Validation
- [ ] T021 Run full test suite `pytest tests/` (must be Green)
- [ ] T022 Update `research/session_log.md` with implementation details
