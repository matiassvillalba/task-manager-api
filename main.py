from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="A lightweight REST API for managing tasks.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Task Manager API is running"}
