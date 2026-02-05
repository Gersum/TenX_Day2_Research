# skill_transaction

## Purpose
Execute budget-checked financial actions via MCP coinbase tool.

## Input
```json
{
  "tenant_id": "uuid-v4",
  "action": "native_transfer | token_issue | balance_check",
  "amount": "string",
  "currency": "USDC",
  "recipient": "wallet_address",
  "dry_run": true
}
```

## Output
```json
{
  "status": "APPROVED | REJECTED | DRY_RUN",
  "tx_hash": "string",
  "reason": "string"
}
```
