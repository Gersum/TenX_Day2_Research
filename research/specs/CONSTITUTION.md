# Chimera Project Constitution

## 1. Core Mission
To build a scalable, autonomous influencer network that leverages Agentic Commerce and Swarm Orchestration to disrupt the traditional digital talent agency model.

## 2. Development Principles (SDD)
- **Spec First**: No implementation code until the interface and logic are ratified in the `research/specs/` directory.
- **Traceability**: Every significant design decision must be recorded in the `session_log.md`.
- **Git Hygiene**: Commits must serve as a narrative of evolving complexity.

## 3. Engineering Standards
- **Component Isolation**: Use the Hub-and-Spoke model with MCP to ensure that core reasoning (Agents) is decoupled from external tools (MCP Servers).
- **Self-Healing**: Design for "Management by Exception." Agents must attempt to resolve common API or logic failures autonomously.
- **Financial Security**: Agentic Commerce via AgentKit must be budget-gated and require high-confidence scores from a "Judge" agent.

## 4. Interaction Guidelines
- **AI-to-AI Protocols**: Communication between agents must use cryptographic signatures (Identity) and standardized JSON schemas (Exchange).
- **Human-in-the-Loop**: High-risk actions (Publishing, Spending > 10% Budget) require human ratification via the Orchestrator dashboard.
