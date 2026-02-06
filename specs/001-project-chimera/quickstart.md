# Quickstart: Project Chimera Core System

## Validation Scenarios

### 1. Verify Task Lifecycle
- **Goal**: Confirm a defined Task can be modeled, serialized, and deserialized.
- **Command**: `pytest tests/test_models.py::test_task_serialization`
- **Success**: JSON output matches `contracts/task.schema.json`.

### 2. Verify Tenant Isolation
- **Goal**: Ensure logic rejects data without valid `tenant_id`.
- **Command**: `pytest tests/test_security.py::test_missing_tenant_id`
- **Success**: Raises `TenantRequiredError`.

### 3. Verify Budget Gating
- **Goal**: Confirm transaction > threshold triggers rejection/escalation.
- **Command**: `pytest tests/test_governance.py::test_excessive_budget`
- **Success**: Returns `Evaluation(verdict=ESCALATE)`.

## Prerequisites
- Python 3.11+
- `uv` package manager
- Redis (optional for unit tests, mocked by default)
