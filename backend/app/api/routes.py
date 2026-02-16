from fastapi import APIRouter, HTTPException
from app.models.task import TaskCreate, TaskUpdate, Task
from app.services.task_service import (
    list_tasks, create_task, get_task, update_task, delete_task
)

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
def api_list_tasks():
    return list_tasks()

@router.post("/tasks", response_model=Task, status_code=201)
def api_create_task(payload: TaskCreate):
    # Intentionally minimal validation; gaps exist for future issues.
    return create_task(payload)

@router.get("/tasks/{task_id}", response_model=Task)
def api_get_task(task_id: int):
    t = get_task(task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return t

@router.patch("/tasks/{task_id}", response_model=Task)
def api_update_task(task_id: int, payload: TaskUpdate):
    t = update_task(task_id, payload)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return t

@router.delete("/tasks/{task_id}", status_code=204)
def api_delete_task(task_id: int):
    ok = delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
