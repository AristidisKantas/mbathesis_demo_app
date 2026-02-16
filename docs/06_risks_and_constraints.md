# Risks & Constraints (Thesis Context)

## Constraints
- Repository is public
- No proprietary corporate information
- Must support reproducible experiments (same prompts, comparable outputs)

## Primary risks
- Scope creep: demo app grows too large
- Agent produces plausible but incorrect issues (hallucination risk)
- Dependency graph errors (missing or wrong ordering)
- Inconsistent estimates if rules not enforced

## Mitigations (expected)
- Keep a stable architecture doc and DoD
- Enforce structured issue schema (dependencies + effort)
- Log retrieved context and agent outputs per run
- Compare baselines: no-RAG vs docs-only vs full-RAG
