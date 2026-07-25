from fastapi import FastAPI, status

from schemas import TaskCreate, TaskResponse

app = FastAPI(
    title="Task Manager API",
    description="A lightweight REST API for managing tasks.",
    version="1.0.0",
)

# Base de datos en memoria (lista temporal para guardar las tareas)
tasks_db: list[dict] = []
task_id_counter = 1


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Task Manager API is running"}


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global task_id_counter

    # Convertimos los datos validados por Pydantic a un diccionario de Python
    new_task = task.model_dump()

    # Asignamos el ID único autoincremental
    new_task["id"] = task_id_counter

    # Guardamos la nueva tarea en la lista
    tasks_db.append(new_task)

    # Incrementamos el contador para la próxima tarea
    task_id_counter += 1

    return new_task
