# Core System Interfaces

## Overview
This document defines the strict interfaces (Inputs/Outputs) for the Chimera Swarm components. These specs must be ratified before implementation.

## 1. Domain Object Schemas (JSON/Pydantic)

### 1.1 Task
The atomic unit of work described by the Planner and executed by the Worker.
```json
{
  "id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "goal_id": "uuid-v4",
  "type": "RESEARCH | CONTENT | REVIEW | ACTION",
  "description": "Natural language description of what needs to be done.",
  "status": "PENDING | ASSIGNED | COMPLETED | FAILED",
  "priority": 1-5,
  "context": {
    "target_platform": "twitter",
    "constraints": ["max_length: 280", "tone: witty"]
  },
  "created_at": "ISO-8601"
}
```

### 1.2 Result
The output produced by a Worker.
```json
{
  "task_id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "worker_id": "agent-id",
  "content": "The actual output (text, image_url, json).",
  "artifacts": ["path/to/file1", "path/to/file2"],
  "meta_data": {
    "execution_time_ms": 120,
    "tool_calls": ["search_tool", "summarizer"]
  },
  "state_version": "int"
}
```

### 1.3 Evaluation (Judge Output)
The quality assessment of a Result.
```json
{
  "task_id": "uuid-v4",
  "tenant_id": "uuid-v4",
  "judge_id": "judge-agent-1",
  "confidence_score": 0.0-1.0,
  "verdict": "APPROVE | REJECT | ESCALATE",
  "feedback": "Specific instructions on why it failed or passed.",
  "state_version": "int",
  "policy_checks": [
    {"rule": "No hate speech", "passed": true},
    {"rule": "On brand", "passed": true}
  ]
}
```

## 2. Component Interfaces

### 2.1 Planner Interface
- **Input**: `UserGoal` (String)
- **Output**: `List[Task]`
- **Behavior**: Must decompose vague goals into executable, atomic tasks.

### 2.2 Worker Interface
- **Input**: `Task`
- **Output**: `Result`
- **Behavior**: Stateless. Must use MCP tools to execute.

### 2.3 Judge Interface
- **Input**: `Task`, `Result`
- **Output**: `Evaluation`
- **Behavior**: Deterministic policy checking.

## 3. MCP Interfaces
### 3.1 Client Config
```json
{
  "mcpServers": {
    "browser": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```
