# Project Chimera — Master Specification (Meta)

## Vision
Build an autonomous influencer network that scales to 1,000+ agents, each operating as a sovereign digital entity with perception, reasoning, creative expression, and economic agency.

## Constraints
- **Spec-Driven**: Implementation must follow specs/ as source of truth.
- **Safety**: Governance, HITL, and policy enforcement are mandatory.
- **Scalability**: Horizontal scale; shared‑nothing workers; Kubernetes‑ready.
- **Decoupling**: All external actions must use MCP (no direct API calls).
- **Traceability**: All major decisions are logged in research/session_log.md.

## Success Criteria
- Agents maintain consistent persona across long horizons.
- Fleet can be managed by a single Super‑Orchestrator.
- Economic actions are budget‑gated and auditable.
