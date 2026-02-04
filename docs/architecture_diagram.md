# Project Chimera Architecture Visualization

This document visualizes the "FastRender Swarm" architecture and the system topology for Project Chimera.

## High-Level System Architecture

```mermaid
graph TD
    %% Clients
    User[User / Client] -->|Goal Submission| API[API Gateway / CLI]
    
    %% Core Swarm (FastRender)
    subgraph "Core Swarm (FastRender Pattern)"
        API --> Planner[Planner Agent]
        Planner -->|Decompose| TaskQ[(Redis Task Queue)]
        
        TaskQ -->|Pop| Worker1[Worker Agent 1]
        TaskQ -->|Pop| Worker2[Worker Agent 2]
        TaskQ -->|Pop| Worker3[Worker Agent N]
        
        Worker1 -->|Result| ReviewQ[(Redis Review Queue)]
        Worker2 -->|Result| ReviewQ
        Worker3 -->|Result| ReviewQ
        
        ReviewQ -->|Pop| Judge[Judge Agent]
        Judge -->|Confidence < 0.7| Planner
        Judge -->|Confidence >= 0.7| Aggregator[Result Aggregator]
    end

    %% Data Layer
    subgraph "Data Layer"
        Aggregator --> PG[(PostgreSQL Ledger)]
        Aggregator --> Weaviate[(Weaviate Memory)]
        Planner -.-> Weaviate
        Judge -.-> Weaviate
    end

    %% MCP Ecosystem
    subgraph "MCP Ecosystem (Hub & Spoke)"
        Worker1 <--> MCPHost[MCP Host]
        Worker2 <--> MCPHost
        
        MCPHost <--> Server1[Brave Search MCP]
        MCPHost <--> Server2[Filesystem MCP]
        MCPHost <--> Server3[Memory MCP]
        MCPHost <--> Server4[SQLite MCP]
    end

    %% Styling
    classDef primary fill:#2d3436,stroke:#0984e3,stroke-width:2px,color:#dfe6e9;
    classDef db fill:#2d3436,stroke:#fab1a0,stroke-width:2px,color:#dfe6e9;
    classDef queue fill:#2d3436,stroke:#fdcb6e,stroke-width:2px,color:#dfe6e9;
    
    class Planner,Worker1,Worker2,Worker3,Judge,MCPHost primary;
    class PG,Weaviate db;
    class TaskQ,ReviewQ queue;
```

## Data Flow & Protocol

1.  **Input**: Goal enters via API.
2.  **Planning**: `Planner` breaks goal into atomic `Tasks` (JSON).
3.  **Queuing**: Tasks pushed to `Redis Task Queue`.
4.  **Execution**: `Workers` claim tasks, use `MCP Tools` to execute.
5.  **Review**: Results pushed to `Redis Review Queue`.
6.  **Judgment**: `Judge` evaluates distinct output against acceptance criteria.
    *   **Pass**: Commit to `PostgreSQL` / Update `Weaviate`.
    *   **Fail**: Send feedback to `Planner` for replanning or retry.

## Component Roles

| Component | Responsibility | Tech Stack |
|:---|:---|:---|
| **Planner** | Strategic decomposition, dependency management. | Python, LLM |
| **Worker** | Tactical execution, tool usage. | Python, MCP Client |
| **Judge** | Quality assurance, safety checks, synthesis. | Python, LLM |
| **Redis** | High-speed message bus for async communication. | Redis 7 |
| **PostgreSQL** | Source of truth for ledgers, users, and final artifacts. | Postgres 15 |
| **Weaviate** | Semantic memory, RAG context. | Weaviate |
