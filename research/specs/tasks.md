# Actionable Task List: Phase 1 (Core Swarm)

## 1. Environment & Infrastructure
- [ ] **1.1** Configure `uv` virtual environment and verify Python 3.11+ version.
- [ ] **1.2** Setup Local Redis (or Mock) for Swarm Queueing based on `data_models.md`.
- [ ] **1.3** Verify connection to Tenx MCP Sense for traceability.

## 2. Core Swarm Components (Logic Only)
- [ ] **2.1** Implement Pydantic Schemas for `Task`, `Result`, and `Evaluation` (Ref: `core_interfaces.md`).
- [ ] **2.2** Create the `Planner` logic: Decompose a `Goal` string into `List[Task]` using the Genesis Prompt.
- [ ] **2.3** Create a stateless `Worker` class capable of popping tasks from Redis and processing them.
- [ ] **2.4** Create the `Judge` logic: Evaluate `Results` against the confidence threshold (0.7) and policy rules.

## 3. MCP & Commerce Integration
- [ ] **3.1** Implement `MCPClient` to manage dynamic tool connections via Stdio.
- [ ] **3.2** Integrate `Coinbase AgentKit` stub for wallet initialization and budget checks.
- [ ] **3.3** Connect `Worker` to `MCPClient` for tool-assisted task execution.

## 4. Testing & Validation
- [ ] **4.1** Write Unit Tests for the Swarm execution loop (Planner -> Redis -> Worker -> Redis -> Judge).
- [ ] **4.2** Perform a "Dry Run" mock goal to verify the sequence diagram in `architecture_strategy.md`.
- [ ] **4.3** Review test coverage (>80%) and document findings in `session_log.md`.
