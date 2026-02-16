from pydantic import BaseModel, Field
from typing import Literal

Status = Literal["todo", "doing", "done"]
Priority = Literal["low", "medium", "high"]

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    description: str = Field(default="", max_length=4000)
    priority: Priority = "medium"

    # NOTE: Intentionally not fully constrained to allowed story points yet,
    # to create an opportunity for an agent-generated issue.
    effort_sp: int = 3

    dependencies: list[int] = Field(default_factory=list)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=4000)
    status: Status | None = None
    priority: Priority | None = None
    effort_sp: int | None = None
    dependencies: list[int] | None = None

class Task(TaskBase):
    id: int
    status: Status = "todo"
    created_at: str
