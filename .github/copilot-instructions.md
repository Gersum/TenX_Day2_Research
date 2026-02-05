# Project Chimera — Copilot Instructions (Mirrored)

## Project Context
This is Project Chimera, an autonomous influencer system.

## Prime Directive
NEVER generate code without checking specs/ first.

## Traceability
Explain your plan before writing code.

## Operating Mode
- Prefer precise, minimal changes over broad refactors.
- Avoid assumptions; verify with specs or ask a focused question.
- Keep user‑visible output concise.

## Spec Hierarchy (Order of Authority)
1. specs/_meta.md (master vision/constraints)
2. specs/functional.md and specs/technical.md
3. research/specs/ (governance, orchestration, commerce, MCP, data models)
4. skills/ (runtime capability contracts)

If there is any conflict, follow the highest‑priority spec and document the conflict in research/session_log.md.

## Required Pre‑Checks (Before Any Code)
- Read the relevant files in specs/ and research/specs/.
- Confirm constraints (safety, HITL, MCP‑only actions, budget gating).
- If unclear, ask a targeted question rather than guessing.
- Identify the source of truth for each requirement.

## Execution Workflow
1. Summarize the task in 1–2 lines.
2. List the exact files you will touch.
3. Describe the change in bullet points.
4. Implement the change.
5. Validate (lint/tests if present).
6. Report results with file links.

## Communication Rules
- State what you will do before doing it.
- If blocked, explain the blocker and the minimal info needed.
- Never claim work is done without evidence.

## Safety & Governance
- No direct API calls. All external actions must use MCP Tools.
- Respect HITL and sensitive‑topic escalation rules.
- Enforce Judge/CFO Judge approval gates for content and financial actions.
- Never bypass governance to “speed up” delivery.

## Data & Security
- Never log secrets or tokens in files.
- Use placeholders for API keys and note required env vars.
- Prefer non‑destructive changes; avoid deleting specs.
- Treat tenant data as isolated by default.

## Documentation Discipline
- Keep specs updated when behavior changes.
- Add or update skills contracts when new capabilities are introduced.
- Update research/session_log.md for major decisions.
- Document any spec gaps found during implementation.

## Testing & Verification
- If tests exist, run relevant ones after changes.
- If no tests exist, state the manual verification performed.

## Tool Use Discipline
- Use editor/file tools for changes; avoid shell edits unless requested.
- Prefer reading larger file sections over many small reads.
- Do not run destructive commands without explicit approval.

## Response Style
- Keep responses short and impersonal.
- Link to files when referencing changes.
