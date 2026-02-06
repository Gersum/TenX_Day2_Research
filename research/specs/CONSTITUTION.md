<!--
SYNC IMPACT REPORT
Version: 0.0.0 -> 1.0.0
Change Type: MAJOR (Initial Ratification of Spec Kit Format)

Modified Principles:
- Reorganized 'Development Principles' into Article I & II
- Reorganized 'Engineering Standards' into Article III, IV, & V
- Reorganized 'Interaction Guidelines' into Article VI & VII
- Reorganized 'Governance Standards' into Article VIII

Added Sections:
- Governance (Amendment Process, Versioning)
- Metadata Header

Pending/TODOs:
- None
-->

# Project Chimera Constitution

**Version**: 1.0.0
**Ratification Date**: 2026-02-06
**Last Amended Date**: 2026-02-06

## Preamble
To build a scalable, autonomous influencer network that leverages Agentic Commerce and Swarm Orchestration to disrupt the traditional digital talent agency model.

## Article I: Spec-Driven Development (SDD)
No implementation code shall be written until the interface, logic, and architecture are ratified in the `specs/` directory. The specification is the source of truth; code is a derived artifact.

## Article II: Traceability & Hygiene
All significant design considerations must be documented in `research/session_log.md`. Git commits must serve as a legible narrative of evolving complexity, not just a save point.

## Article III: Component Isolation (Hub-and-Spoke)
The system MUST use the Hub-and-Spoke model with MCP. Core reasoning (Agents) MUST be decoupled from external tools (MCP Servers) to ensure portability and security.

## Article IV: Self-Healing Systems
Design for "Management by Exception." Agents must attempt to resolve common API or logic failures autonomously before escalating to human operators.

## Article V: Financial Security & Budget Gating
Agentic Commerce (AgentKit) MUST be budget-gated. Any transaction requires a high-confidence score from a "Judge" agent and strict adherence to the `BudgetGuard` logic.

## Article VI: Protocol-First Interaction
Communication between agents MUST use cryptographic signatures for identity and standardized JSON schemas for information exchange. No unstructured chatter between system components.

## Article VII: Human-in-the-Loop (HITL)
High-risk actions, specifically Publishing content and Spending > 10% of the daily budget, REQUIRE human ratification via the Orchestrator dashboard.

## Article VIII: Operational Compliance
All governance rules ratified in `research/specs/` are binding. The BoardKit Policy Hub (`AGENTS.md`) serves as the definitive source for brand voice, ethics, and operational constraints.

## Governance

### Amendment Process
1. **Proposal**: Create a PR with a `docs: amend constitution` commit.
2. **Review**: Requires approval from the Lead Architect (User) and the CFO Judge (Simulator).
3. **Ratification**: Merge to main increments the version number.

### Versioning Policy
- **MAJOR**: Backward incompatible governance/principle removals or redefinitions.
- **MINOR**: New principle/section added or materially expanded guidance.
- **PATCH**: Clarifications, wording, typo fixes.

### Compliance
All architectural decisions and code reviews MUST reference specific Articles of this Constitution to justify choices.
