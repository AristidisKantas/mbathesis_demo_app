import json
from datetime import datetime, timezone
from app.db.session import get_conn
from app.models.task import TaskCreate, TaskUpdate, Task

def _row_to_task(row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
        effort_sp=row["effort_sp"],
        dependencies=json.loads(row["dependencies_json"]),
        created_at=row["created_at"],
    )

def list_tasks() -> list[Task]:
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM tasks ORDER BY id ASC").fetchall()
    return [_row_to_task(r) for r in rows]

def create_task(payload: TaskCreate) -> Task:
    now = datetime.now(timezone.utc).isoformat()

    # TODO: enforce allowed effort_sp values (1,2,3,5,8,13)
    # TODO: prevent dependency cycles
    # TODO: validate dependencies exist

    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO tasks(title,description,status,priority,effort_sp,dependencies_json,created_at) VALUES (?,?,?,?,?,?,?)",
            (payload.title, payload.description, "todo", payload.priority, payload.effort_sp,
             json.dumps(payload.dependencies), now)
        )
        conn.commit()
        task_id = cur.lastrowid

        row = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
    return _row_to_task(row)

def get_task(task_id: int) -> Task | None:
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
    return _row_to_task(row) if row else None

def update_task(task_id: int, payload: TaskUpdate) -> Task | None:
    existing = get_task(task_id)
    if not existing:
        return None

    data = existing.model_dump()
    upd = payload.model_dump(exclude_unset=True)
    data.update({k: v for k, v in upd.items() if v is not None})

    # TODO: disallow setting status=done if dependencies are not done
    # TODO: validate dependencies exist
    # TODO: prevent cycles on update

    with get_conn() as conn:
        conn.execute(
            "UPDATE tasks SET title=?, description=?, status=?, priority=?, effort_sp=?, dependencies_json=? WHERE id=?",
            (data["title"], data["description"], data["status"], data["priority"], data["effort_sp"],
             json.dumps(data["dependencies"]), task_id)
        )
        conn.commit()
        row = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
    return _row_to_task(row)

def delete_task(task_id: int) -> bool:
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
    return cur.rowcount > 0
