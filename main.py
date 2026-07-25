from fastapi import FastAPI, HTTPException, status

from schemas import TaskCreate, TaskResponse

app = FastAPI(
    title="Task Manager API",
    description="A lightweight REST API for managing tasks.",
    version="1.0.0",
)

tasks_db: list[dict] = []
task_id_counter = 1


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Task Manager API is running"}


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global task_id_counter

    new_task = task.model_dump()
    new_task["id"] = task_id_counter
    tasks_db.append(new_task)
    task_id_counter += 1

    return new_task


@app.get("/tasks", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks():
    return tasks_db


@app.get(
    "/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK
)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {task_id} not found",
    )


@app.put(
    "/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK
)
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks_db:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {task_id} not found",
    )


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(index)
            return {"message": f"Task with ID {task_id} deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {task_id} not found",
    )
