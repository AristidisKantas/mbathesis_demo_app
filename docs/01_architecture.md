# Architecture (C4-lite)

## System context
A single-user web application:

User -> Frontend (React) -> Backend API (FastAPI) -> SQLite DB

## Components
### Frontend (React + TypeScript)
- Responsible for the board view and basic task interactions
- Talks to backend via REST JSON
- Intentionally minimal UI state management and error handling

### Backend (FastAPI)
Layered structure:
- `api/routes.py`: HTTP boundary (routing + basic validation)
- `services/task_service.py`: business logic
- `db/*`: SQLite persistence utilities
- `models/task.py`: Pydantic models for request/response

### Database (SQLite)
- Local SQLite database stored in `backend/app/app.db`
- Simple schema created by `backend/app/db/init_db.py`
- No migrations framework (intentional gap / tech debt)

## Key design decisions
- REST API for simplicity and tooling support
- Small, readable codebase that supports retrieval-based agents

## Known limitations (intentional)
- Weak validation in some endpoints
- No pagination/filtering yet
- Dependency cycle checks missing
- Tests are minimal
- No CI pipeline

These limitations are designed to create realistic opportunities for planning and issue creation.
