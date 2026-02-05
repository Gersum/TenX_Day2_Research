# OpenClaw Integration (Optional)

## Objective
Publish Chimera agent availability and capabilities to the OpenClaw network.

## Status Publishing
- **Registry Payload**: agent_id, skills, availability, pricing, wallet_address.
- **Frequency**: On boot, then heartbeat every 5 minutes.
- **Discovery**: OpenClaw registry enables other agents to find Chimera services.

## Security
- Sign announcements with AgentKit wallet.
- Allowlist trusted peers via Weaviate reputation index.
