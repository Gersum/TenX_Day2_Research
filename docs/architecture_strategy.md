# Architecture Strategy: FastRender Swarm & Agentic Factory

## Overview
This document outlines the architectural strategy for Project Chimera's "Factory," focusing on the FastRender Swarm pattern, MCP integration, and Agentic Commerce.

## FastRender Swarm Pattern
The core execution engine follows a hierarchical swarm model to ensure quality and scalability.
- **Planner**: Decomposes high-level goals into atomic tasks. Uses "Mock LLM" (initially) to simulate reasoning. Pushes tasks to `task_queue` (Redis).
- **Worker**: Stateless agents that pull tasks from `task_queue`, execute them (simulated work), and push results to `review_queue`.
- **Judge**: Quality assurance agents that pull from `review_queue`, validate against success criteria, and either commit the result (Final) or reject it (Retry). Uses Optimistic Concurrency Control (OCC) for state updates.

## Data Topology (Hybrid DB)
- **Redis**: Fast task queues (Planner -> Worker -> Judge) and caching.
- **PostgreSQL**: Transactional state (User accounts, Agent configurations, Ledgers).
- **Weaviate**: Vector memory for RAG (Research, Persona recall).

## MCP Integration (Model Context Protocol)
- **Architecture**: Hub-and-Spoke.
- **Client**: Chimera Core acts as an MCP Client.
- **Servers**: External tools (Browsing, Social Media, Wallet) are accessed via MCP Servers.
- **Protocol**: Stdio/SSE connections.

## Agentic Commerce
- **Integration**: Coinbase AgentKit.
- **Security**: Non-custodial wallets, ENV key management.
- **Logic**: CommerceManager handles budget checks and onchain ops.

## HITL & Governance
- **Confidence Thresholds**: Low confidence (<0.7) triggers human escalation.
- **Traceability**: All actions logged to Tenx MCP Sense.
