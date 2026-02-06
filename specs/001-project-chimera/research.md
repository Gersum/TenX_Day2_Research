# Research: Project Chimera Core System

## Decisions

### 1. Library-First Architecture
- **Decision**: All core logic resides in `src/chimera_core` as a distributable package.
- **Rationale**: Enforces modularity and allows independent versioning/testing of core logic before app integration.
- **Alternatives**: Monolithic app (rejected due to difficulty in testing agent logic in isolation).

### 2. Pydantic for Data Models
- **Decision**: Use Pydantic v2 for all domain objects (`Task`, `Result`, etc.).
- **Rationale**: Strong typing, runtime validation, and easy serialization to JSON for MCP transport.

### 3. Tenant Isolation Middleware
- **Decision**: Enforce `tenant_id` checks via a Python decorator/middleware pattern at the entry point.
- **Rationale**: Prevents accidental data crossover in a multi-tenant swarm.

### 4. MCP-Only External Actions
- **Decision**: Agents generally cannot call external APIs directly; they must use the MCP Client interface.
- **Rationale**: Centralized audit, rate limiting, and credential management at the MCP server level.

### 5. Two-Stage Governance
- **Decision**: Automated Policy Check (First pass) -> Human Review (Escalation).
- **Rationale**: Optimizes for speed on low-risk tasks while maintaining human oversight for critical actions (High Spend/Publishing).
