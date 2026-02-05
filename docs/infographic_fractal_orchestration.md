# Fractal Orchestration Infographic

```mermaid
graph TD
    %% Top Level
    SO[Super-Orchestrator (Human)] -->|Strategy & Budgets| MA[Manager Agents]
    MA -->|Campaign Plans| SW1[Worker Swarm A]
    MA -->|Campaign Plans| SW2[Worker Swarm B]
    MA -->|Campaign Plans| SWN[Worker Swarm N]

    %% Swarm A
    subgraph "FastRender Swarm (A)"
        PA[Planner] -->|DAG Tasks| TQ[(Redis Task Queue)]
        TQ --> WA1[Worker 1]
        TQ --> WA2[Worker 2]
        WA1 -->|Result| RQ[(Redis Review Queue)]
        WA2 -->|Result| RQ
        RQ --> JA[Judge]
        JA -->|Approve| OUTA[Publish/Commit]
        JA -->|Reject| TQ
        JA -->|Escalate| HITL[Human Review]
        JA --> CFO[CFO Judge]
        CFO -->|Approve Tx| CHAIN[(On-Chain)]
        CFO -->|Reject Tx| TQ
    end

    %% Governance
    BK[BoardKit (Policy/Brand)] --> MA
    BK --> JA
    BK --> CFO

    %% MCP
    subgraph "MCP (USB-C for AI)"
        MCPH[MCP Host]
        MCPH <-->|Tools/Resources| WTOOLS[Search, Files, Commerce]
    end

    WA1 --> MCPH
    WA2 --> MCPH

    %% Infra
    K8S[Kubernetes HPA] --> SW1
    K8S --> SW2
    K8S --> SWN

    classDef human fill:#f1c40f,stroke:#b7950b,color:#2d3436,stroke-width:2px;
    classDef agent fill:#2d3436,stroke:#0984e3,color:#dfe6e9,stroke-width:2px;
    classDef queue fill:#2d3436,stroke:#fdcb6e,color:#dfe6e9,stroke-width:2px;
    classDef policy fill:#2d3436,stroke:#00b894,color:#dfe6e9,stroke-width:2px;
    classDef infra fill:#2d3436,stroke:#e17055,color:#dfe6e9,stroke-width:2px;

    class SO human;
    class MA,PA,WA1,WA2,JA,CFO agent;
    class TQ,RQ queue;
    class BK policy;
    class K8S infra;
```

## Legend
- **Super-Orchestrator**: Human strategy layer.
- **Manager Agents**: Fractal layer orchestrating multiple swarms.
- **FastRender Swarm**: Planner → Worker → Judge execution loop.
- **CFO Judge**: Financial oversight & budget gating.
- **BoardKit**: Centralized policy/brand governance.
- **MCP**: Standardized interface for tools/resources.
- **Kubernetes**: Scales swarms to 1,000+ concurrent agents.
