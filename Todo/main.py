from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.todo import ToDo
from typing import List

app = FastAPI()

class TodoTask(BaseModel):
    todos: List[ToDo]

to_do = []

@app.post("/todos/")
async def Create_tasks(todos: List[ToDo]):
    for todo in todos:
        to_do.append(todo)
    return {"message": "To-Do list created"}

@app.get("/todos/")
async def Get_all_tasks():
    return {"todos": to_do}

@app.delete("/todos/{task_no}")
async def Delete_tasks(task_no: int):
    for i, t in enumerate(to_do):
        if t.no == task_no:
            del to_do[i]
            return {"message": "To-Do task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")