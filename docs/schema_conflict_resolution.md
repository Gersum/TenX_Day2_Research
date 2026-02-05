# Schema Conflict Resolution

This document lists schema conflicts across the repo and the canonical resolution. Update the referenced files to match `specs/canonical_schemas.md`.

## Canonical Source
- `specs/canonical_schemas.md`

## Resolved Conflicts

1. `specs/technical.md`
- `priority`: clarified as integer 1–5 inclusive.
- `meta_data`: renamed to `metadata`.
- `state_version`: standardized as integer.
- `schema_version`: added to schema payloads.

2. `research/specs/core_interfaces.md`
- `priority`: standardized to integer 1–5 inclusive (example shown as integer).
- `state_version`: standardized as integer.
- `meta_data`: renamed to `metadata`.
- `schema_version`: added to schema payloads.

3. `research/specs/agent_prompts.md`
- References updated to `specs/canonical_schemas.md`.

4. `research/specs/tasks.md`
- References updated to `specs/canonical_schemas.md`.

## Optional Cleanups (Non-blocking)
- Consider removing duplicate schema definitions in `research/specs/core_interfaces.md` and replacing with a link to the canonical spec.
