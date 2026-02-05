# Core Functional Systems Specification

## Purpose
Define the modular functional systems that transform scripted influencers into autonomous agents.

## 1. Cognitive Core & Persona Management
- **SOUL.md Persona DNA**: Immutable identity file (backstory, tone, values).
- **RAG Pipeline**: Context assembly uses SOUL.md + memory retrieval.
- **Hierarchical Memory**:
  - **Episodic (Short‑Term)**: Redis cache for immediate context.
  - **Semantic (Long‑Term)**: Weaviate vector memory for months‑long recall.

## 2. Perception System (Data Ingestion)
- **Resource Polling**: Agents continuously monitor MCP Resources (news, mentions).
- **Semantic Filtering**: Ingested content must pass a relevance filter (e.g., Gemini 3 Flash) scored against active goals before task creation.

## 3. Creative Engine & Action System
- **Multimodal Generation**: Use MCP tools for text, image, and video generation.
- **Character Consistency Lock**: Image generation must include a `character_reference_id` to maintain visual identity.
- **Bi‑Directional Interaction Loop**: Social actions route through MCP, rate‑limited and logged, then gated by Judge approval.

## 4. Agentic Commerce
- **Economic Agency**: Coinbase AgentKit wallet per agent (non‑custodial).
- **Autonomous Transactions**: On‑chain transfers, token issuance, P&L tracking.
- **CFO Judge**: Reviews all financial requests against budget and safety policies.

## 5. Orchestration & Swarm Governance
- **Planner‑Worker‑Judge**: Decompose, execute, validate.
- **OCC Enforcement**: Judge validates `state_version`; stale results are rejected and re‑queued.
