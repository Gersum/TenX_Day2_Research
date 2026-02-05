# Agentic Commerce Specification

## 1. Economic Agency
Agents are equipped with non-custodial wallets (Coinbase AgentKit + Agentic Commerce Protocols) enabling:
- Onchain transactions
- Budgeted tool purchases
- Revenue tracking and P&L statements
- Autonomous deal negotiation within approved policy boundaries
- Asset purchases required for operations (e.g., compute credits, API quotas)
- Balance checks for ongoing financial health

## 1.2 Ledgering & Networks
- **Immutable Ledger**: All financial transactions are recorded on-chain.
- **Supported Networks**: Base, Ethereum, or Solana (network chosen per tenant policy).

## 1.1 Wallet Requirements
- **Non-custodial Wallets**: Each agent has a unique, persistent wallet address.
- **Secrets Management**: Wallet secrets must be stored in enterprise-grade secret storage (no plaintext keys), e.g., AWS Secrets Manager or HashiCorp Vault.

## 2. Budget Gating
- Every agent has a daily and monthly spend limit.
- Transactions above 10% of budget require Judge approval.
- **Resource Governor**: Enforces hard caps on inference and media generation costs to prevent runaway spend.

## 3. Allowed Transactions
- API usage fees
- Collaboration bounties
- Sponsored content revenue capture
- **On-chain transfers** (e.g., ETH/USDC payments to service providers)
- **Token issuance** (e.g., ERC-20 fan loyalty programs) when approved

## 4. Prohibited Transactions
- Transfers to unknown wallets
- High-risk DeFi protocols
- Unverified contracts

## 5. Governance & Safeguards
- **CFO Judge Agent**: Specialized financial gatekeeper reviews all transaction requests.
- **Anomaly Detection**: Rejects suspicious or high-risk transactions automatically.
- **Sensitive Topic HITL**: Financial advice or sensitive transfers require human review.

## 6. Agent P&L Management
- Agents maintain autonomous **Profit & Loss (P&L)** statements as first-class artifacts.
- Budget status must be surfaced to the Orchestrator dashboard for fleet-wide monitoring.

## 7. Auditability
- Every transaction logged in PostgreSQL ledgers.
- All signatures use wallet address identity.
- Orchestrator dashboard aggregates fleet P&L and financial health.

## 8. Cost Discipline (Opex)
- LLM inference and media generation are treated as operating expenses (Opex).
- Resource Governor enforces caps to avoid runaway costs.
