# Architecture Readiness Checklist

This checklist is for **architecture-stage readiness** (pre-implementation). Use it as a gate before moving into build.

## 1. Canonical Definitions
- [ ] Canonical schemas defined in one place and referenced everywhere else.
- [ ] Schema versioning policy documented.
- [ ] Contract test plan defined for schema validation.

## 2. Scope and Boundaries
- [ ] MVP scope explicitly defined (what is in/out for the next milestone).
- [ ] Must-have vs nice-to-have features labeled.
- [ ] External dependencies listed with fallback behavior.

## 3. System Architecture
- [ ] Component boundaries and responsibilities defined.
- [ ] End-to-end sequence diagram or state machine documented.
- [ ] Data flow and control flow separated (action vs governance paths).

## 4. Governance and Safety
- [ ] HITL thresholds and sensitive-topic policies defined.
- [ ] Financial governance policy and approval flows defined.
- [ ] Audit log format and retention policy documented.

## 5. Data and Storage
- [ ] Primary data store(s) chosen with rationale.
- [ ] Consistency and concurrency rules defined.
- [ ] Migration and versioning strategy defined.

## 6. Observability and Reliability
- [ ] Event logging schema defined.
- [ ] Retry and escalation semantics defined.
- [ ] Failure modes and recovery paths documented.

## 7. Security and Compliance
- [ ] Secrets management strategy documented.
- [ ] Tenant isolation model documented.
- [ ] PII handling policy documented.

## 8. Operational Readiness
- [ ] Environment configuration schema defined.
- [ ] CI/CD expectations defined for lint, type check, test, security.
- [ ] Performance SLOs defined with measurement method.
