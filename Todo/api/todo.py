from pydantic import BaseModel
from typing import List


class ToDo(BaseModel):
    no: int
    task: str
    description: str = None
    completed: bool = False



