# Feature Spec: Project Chimera Core System

## Summary
Establish the core specification set for Project Chimera, an autonomous influencer network that operates with strict governance, MCP-only external actions, and tenant isolation.

## Goals
- Define the system scope, roles, and safety constraints for the initial Chimera MVP.
- Provide testable functional and technical requirements that drive future implementation.
- Ensure alignment with Spec-Driven Development workflow and traceability.

## Non-Goals
- Full implementation of the agent swarm runtime.
- Production deployment or scaling automation.
- UI/UX design for operator dashboards.

## User Stories
- As a Planner, I want goals decomposed into atomic tasks so workers can execute in parallel.
- As a Worker, I want to fetch trends from MCP resources so I can draft content quickly.
- As a Judge, I want to validate outputs against safety and persona rules before publishing.
- As a CFO Judge, I want to approve transactions based on budget policy.
- As a Super-Orchestrator, I want a dashboard view of fleet health, costs, and approvals.
- As a Brand Owner, I want tenant data isolated from other clients.

## Functional Requirements
- The system must enforce MCP-only external actions.
- The system must support HITL and governance escalation paths.
- The system must provide role-based workflows for Planner, Worker, Judge, and CFO Judge.
- The system must persist task, result, and evaluation artifacts with tenant scoping.

## Non-Functional Requirements
- Support 1,000+ concurrent agents.
- High-priority actions complete in under 10 seconds.
- All external actions are audited and traceable.

## Data and Interfaces
- Task/Result/Evaluation schemas are defined in specs/technical.md.
- Core interfaces and data models are defined in research/specs/core_interfaces.md and research/specs/data_models.md.

## Risks and Open Questions
- Resolved: Initial platform targets are Twitter (Text) and YouTube (Video), accessed via MCP tools.
- Resolved: Governance workflow is Two-Stage: 1. Auto-Policy Check (Safety/Budget), 2. Human Review for high-risk actions.

## Acceptance Criteria
- [ ] Spec aligns with specs/_meta.md constraints.
- [ ] All user stories map to at least one functional requirement.
- [ ] Referenced schemas are traceable in specs/technical.md.
