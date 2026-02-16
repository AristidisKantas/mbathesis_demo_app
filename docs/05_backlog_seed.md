# Backlog Seed (Intentionally Unstructured)

These are rough ideas, intentionally not well-formed. They exist to be transformed into structured GitHub Issues.

- Add pagination to GET /tasks
- Add filtering by status and priority
- Enforce effort_sp allowed values
- Improve validation: title length, required fields
- Prevent dependency cycles
- Disallow marking a task as done when dependencies are not done
- Add endpoint to bulk update task status
- Add endpoint to import tasks from JSON (seed data)
- Add export tasks to JSON
- Add search by keyword (title/description)
- Add a simple priority scoring rule (WSJF-lite)
- Add sprint entity schema (no UI yet)
- Add sprint planning endpoint (assign tasks to sprint)
- Add board UI swimlanes and better columns
- Add dependency visualization on UI (simple list)
- Add loading/error states in UI
- Improve API error responses (consistent shape)
- Add CI workflow (pytest + frontend build)
- Add Docker compose for local run
- Improve test coverage for task_service
