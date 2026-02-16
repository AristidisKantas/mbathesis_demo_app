from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MBA Thesis Demo App - Mini Backlog Manager")
app.include_router(router)
