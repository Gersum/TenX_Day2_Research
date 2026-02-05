# skill_social_publish

## Purpose
Publish or schedule social content via MCP tools.

## Input
```json
{
  "tenant_id": "uuid-v4",
  "platform": "twitter | instagram | tiktok",
  "content": "string",
  "media_urls": ["url"],
  "dry_run": true
}
```

## Output
```json
{
  "status": "PUBLISHED | QUEUED | DRY_RUN",
  "post_id": "string",
  "warnings": ["string"]
}
```
