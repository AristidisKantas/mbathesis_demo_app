# API Specification

Base URL: `http://localhost:8001`

## Endpoints

### GET /tasks
Returns all tasks.

Response (200):
```json
[
  {
    "id": 1,
    "title": "Set up DB schema",
    "description": "Create SQLite schema for tasks",
    "status": "todo",
    "priority": "high",
    "effort_sp": 3,
    "dependencies": [],
    "created_at": "2026-02-16T10:00:00Z"
  }
]


POST /tasks

Req:
{
  "title": "Implement GET /tasks",
  "description": "Return list of tasks",
  "priority": "medium",
  "effort_sp": 2,
  "dependencies": [1]
}

Resp(201):
{
  "id": 2,
  "title": "Implement GET /tasks",
  "description": "Return list of tasks",
  "status": "todo",
  "priority": "medium",
  "effort_sp": 2,
  "dependencies": [1],
  "created_at": "2026-02-16T10:05:00Z"
}


GET /tasks/{id}

Returns a single task (404 if not found).

PATCH /tasks/{id}

Partial update.
Fields allowed: title, description, status, priority, effort_sp, dependencies.

DELETE /tasks/{id}

Deletes a task.

Error model (basic)

400: invalid input

404: not found

500: server error

This is intentionally basic and can be improved via future issues.


### 3.5 `docs/04_quality_standards.md`
```md
# Quality Standards & Definition of Done (DoD)

## Coding standards
- Prefer clarity over cleverness
- Keep functions small and testable
- Follow consistent naming and folder structure

## Estimation (Story Points)
Allowed values: **1, 2, 3, 5, 8, 13**

Guideline:
- 1: trivial (small UI tweak)
- 2–3: small feature or bug fix with tests
- 5: moderate change across layers
- 8: larger feature or refactor
- 13: avoid; break down further if possible

## Definition of Done (DoD)
A work item is done when:
1. Acceptance criteria are met
2. Dependencies are respected and documented
3. Tests are added OR a clear test plan is documented
4. Docs updated if API/UX changes
5. Basic error handling is included

## Testing expectations
- Backend: unit tests for `services/`, API tests for routes
- Frontend: basic component behavior tests (optional; may be added later)

## Issue requirements (for agent-generated issues)
Every issue should include:
- clear description and scope
- acceptance criteria (at least 2 bullet items)
- **dependencies** (at least 1, even if “depends on discovery/spike”)
- effort estimate in story points
