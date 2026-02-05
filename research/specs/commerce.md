# Agentic Commerce Specification

## 1. Economic Agency
Agents are equipped with non-custodial wallets (Coinbase AgentKit) enabling:
- Onchain transactions
- Budgeted tool purchases
- Revenue tracking and P&L statements

## 2. Budget Gating
- Every agent has a daily and monthly spend limit.
- Transactions above 10% of budget require Judge approval.

## 3. Allowed Transactions
- API usage fees
- Collaboration bounties
- Sponsored content revenue capture

## 4. Prohibited Transactions
- Transfers to unknown wallets
- High-risk DeFi protocols
- Unverified contracts

## 5. Auditability
- Every transaction logged in PostgreSQL ledgers.
- All signatures use wallet address identity.
