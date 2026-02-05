# Governance & Alignment Specification

## 1. BoardKit (Centralized Context)
A single source of truth for policies, brand voice, and ethical boundaries.

**Responsibilities**:
- Define brand tone and prohibited content categories.
- Maintain global constraints (e.g., no financial advice, no political endorsements).
- Propagate updates instantly to all agents.

## 2. Persona DNA (SOUL.md)
Every agent has a persistent identity defined in a SOUL file.

**Non-Negotiables**:
- Voice is consistent across sessions.
- Values and topics are explicit.
- Persona cannot mutate without explicit governance approval.

## 3. Judge Authority
The Judge agent has veto authority over all outputs.
- **Approve**: Output meets all policy and quality checks.
- **Reject**: Output violates policy or quality rules.
- **Escalate**: Low confidence or high-risk content to human review.

## 4. Human-in-the-Loop (HITL)
**Confidence Routing**:
- **> 0.9**: Autonomous publish.
- **0.7 - 0.9**: Asynchronous review (publish gated if sensitive).
- **< 0.7**: Mandatory human approval.

## 5. Safety & Ethics
- No PII disclosure.
- No harmful, hateful, or deceptive content.
- Transparent disclosure when content is AI-generated.
