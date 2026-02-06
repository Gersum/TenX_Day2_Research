# Plan: Project Chimera Core System

## Objective
Translate the Chimera core specification into an actionable, test-first implementation roadmap.

## Scope
- In scope:
  - Core agent roles and governance workflows.
  - MCP-only tool routing and auditability constraints.
  - Baseline data models and contracts for tasks/results/evaluations.
- Out of scope:
  - Full production deployment.
  - Advanced analytics dashboards.

## Architecture & Technology
- **Language**: Python 3.11+
- **Data Models**: Pydantic v2 (See `data-model.md`)
- **Isolation**: Tenant-scoped Middleware
- **Governance**: Two-stage (Auto + HITL)
- **External Interfaces**: MCP Client Protocol (See `research.md`)

## Constitution Assessment
- **Library-First**: Plan builds `src/chimera_core` first.
- **Test-First**: Task list explicitly mandates failing tests before implementation.
- **Simplicity**: No complex microservices yet; modular library structure.

## Milestones
1. **Models & Contracts**: Validate `contracts/` with Pydantic models (Test Cycle 1).
2. **Core Logic**: Implement `TenantContext` and `BudgetGuard` (Test Cycle 2).
3. **Agent Interfaces**: Implement abstract base classes and logic mocks (Test Cycle 3).


## Dependencies
- specs/_meta.md, specs/functional.md, specs/technical.md
- research/specs/governance_alignment.md
- research/specs/orchestration.md

## Risks
- Governance requirements may expand beyond current scope.
- MCP tool availability and permissions may delay execution.

## Validation
- Tests derived from contracts pass in CI.
- Spec-check script reports no missing required spec artifacts.
