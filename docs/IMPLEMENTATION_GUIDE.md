# Implementation Compatibility Guide (Agent/Human)

**Date**: 2026-02-06
**Version**: 1.0 (Phase 1 Complete)
**Context**: Project Chimera Feature 001 (Core System)
**Primary User**: Implementation Agents (Model/Human)

---

## 1. System Architecture & Constraints

### 1.1 The Prime Directive
**Strict Spec-Driven Development (SDD)** is enforced.
- **Rule 1**: Implementation MUST strictly follow `specs/001-project-chimera/tasks.md`.
- **Rule 2**: No code is written unless a spec exists in `specs/` and a task exists in `tasks.md`.
- **Rule 3**: Tests MUST be written FIRST (Task T005 is done (Red), T006 is implementation).

### 1.2 Architectural Pattern
**Hub-and-Spoke with Tenant Isolation**.
- **Hub**: `src/chimera_core` (Pure Python Library).
- **Spokes**: `src/chimera_core/mcp` (MCP Client wrappers).
- **Isolation**: Middleware (`TenantContext`) using `contextvars`.
- **Constraint**: **NO** shared global state that isn't tenant-scoped.

## 2. Repository Map

| Path | Description | usage_rule |
| :--- | :--- | :--- |
| **`specs/001-project-chimera/`** | **Requirements Source**. | READ-ONLY. Do not modify unless instructed to "Clarify". |
| **`contracts/`** | **Interface definitions**. | READ-ONLY. Use these JSON schemas to validate Pydantic models. |
| **`checklists/`** | **Verification Rules**. | READ-ONLY. Use to self-correct before finishing a task. |
| **`src/chimera_core/`** | **Implementation**. | WRITE. The library code resides here. |
| **`tests/`** | **Verification**. | WRITE (New Tests) / EXECUTE (Regressions). |
| **`.specify/memory/`** | **Project Memory**. | READ. Constitution and Voice. |
| **`research/session_log.md`** | **Audit Trail**. | APPEND-ONLY. Log every major implementation step. |

## 3. Current Implementation State

**Phase**: Foundational / Security Kernel (Phase 2)
**Status**: **RED (Failing Tests)**

### Active Context
1.  **Failing Test**: `tests/core/test_security.py`
    *   Error: `ModuleNotFoundError: No module named 'chimera_core.security'`
    *   Intent: Validates the existence and isolation logic of `TenantContext`.
2.  **Next Required Action**: Implement `src/chimera_core/security.py`.

## 4. Execution Protocol for Agents

When implementing tasks, follow this loop strictly:

1.  **Context Loading**:
    *   Read `specs/001-project-chimera/tasks.md` to identify the current task.
    *   Read `specs/001-project-chimera/spec.md` for functional logic.
    *   Read `contracts/` for data schemas.

2.  **Test-Driven Execution**:
    *   IF `make test` PASSES: Write a FAILING test for the current requirement.
    *   IF `make test` FAILS: Write MINIMAL code to pass the test.

3.  **Verification**:
    *   Run `make test` (encapsulated in Docker).
    *   Ensure 100% pass rate before marking task done.

4.  **Logging**:
    *   Append a summary of changes to `research/session_log.md`.

## 5. Technical Specifications (Frozen)

### Security Kernel (`T006`)
*   **Class**: `TenantContext`
*   **Location**: `src/chimera_core/security.py`
*   **Mechanism**: Python `contextvars.ContextVar`.
*   **API**:
    *   `set_tenant(tenant_id: str)`
    *   `get_current_tenant() -> str` (Raises `MissingTenantError` if empty)
    *   `reset_context()`

### Data Models (`T008`)
*   **Base**: Pydantic `BaseModel`.
*   **Compliance**: Must validate against schemas in `contracts/`.

## 6. Project Checklist Links
*   [Compliance Checklist](specs/001-project-chimera/checklists/governance.md)
*   [Implementation Plan](specs/001-project-chimera/plan.md)
