# skill_trend_discovery

## Purpose
Discover and summarize trending topics from MCP resources.

## Input
```json
{
  "tenant_id": "uuid-v4",
  "sources": ["news://...", "social://mentions"],
  "query": "string",
  "time_window": "ISO-8601"
}
```

## Output
```json
{
  "trends": [
    {"topic": "string", "score": 0.0, "evidence": ["url"]}
  ]
}
```
