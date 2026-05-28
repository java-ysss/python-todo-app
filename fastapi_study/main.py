from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskInput(BaseModel):
    name : str

@app.get("/")
def hello():
    return{"message" : "こんにちは"}

@app.get("/tasks") #「/tasks にGETリクエストが来たらこの関数を実行する」です。
def get_tasks():
    return{"tasks" : ["勉強","運動","散歩"]} #JSONを返す

@app.get("/tasks/{task_id}") #　{task_id}　URLの一部を変数として受け取る
def get_task(task_id : int):
    return {"task_id" : task_id, "name": f"{task_id}番目のタスク"}


@app.post("/tasks")
def create_task(task : TaskInput):
        return{"message" : f"「{task.name}」をついかしました"}


