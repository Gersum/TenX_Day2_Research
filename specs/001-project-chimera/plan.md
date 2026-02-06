# Implementation Plan: Project Chimera Core System

## 1. Executive Summary
This plan details the implementation of the Chimera Core System (Feature 001), adhering to the **Spec-Driven Development (SDD)** and **Library-First** principles ratified in the Constitution v1.0.0.

## 2. Architecture & Technology (Article III)
- **Language**: Python 3.11+ (Enforced via `pyproject.toml`)
- **Structure**: Modular Library (`src/chimera_core`)
- **Dependency Isolation**: Hub-and-Spoke pattern.
  - **Spokes**: MCP Clients (Tools)
  - **Hub**: `ChimeraContext` (State management)
- **State Store**: Redis (Task Queue), PostgreSQL (Ledger - *future*), Weaviate (Memory - *future*).

## 3. Data Integrity Strategy (Article VI)
- **Protocols**: All Agent-to-Agent communication MUST use strict Pydantic v2 models.
- **Contracts**: JSON Schemas in `contracts/` serve as the language-agnostic interface.
- **Validation**: `TenantContext` middleware ensures data isolation at the entry point.

## 4. Work Breakdown (Phased)

### Phase 1: Infrastructure & Contracts (Current)
- [x] Initialize Project Structure (`src/chimera_core`)
- [ ] Define JSON Contracts (`contracts/task.schema.json`)
- [ ] Implement Skeleton Pydantic Models

### Phase 2: Security Kernel (Blocking)
- [ ] Implement `TenantContext` Middleware (Header: `X-Tenant-ID`)
- [ ] Verify Isolation via Tests

### Phase 3: Core Agents (US1, US2)
- [ ] `PlannerAgent`: Decomposition Logic
- [ ] `WorkerAgent`: MCP Tool Bridge

### Phase 4: Governance (US3, US4) (Article V, VII)
- [ ] `JudgeAgent`: Policy Evaluation
- [ ] `BudgetGuard`: Spend Authorization

## 5. Technical Decisions & Trade-offs
- **Tenant ID**: We will use `X-Tenant-ID` HTTP header for context propagation (Option A from Clarification).
- **Orchestrator**: Simple CLI for MVP, evolving to API later.

## 6. Risks & Mitigation
- **Risk**: MCP Tool Latency. **Mitigation**: AsyncIO + Timeout Retries.
- **Risk**: Governance Bottleneck. **Mitigation**: Optimistic approval for low-risk (<$1) actions.

## 7. Verification
- **TDD**: Tests MUST fail before implementation is written.
- **Coverage**: 100% Line Coverage on `security.py` and `governance.py`.
