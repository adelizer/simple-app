from pydantic import BaseModel
from fastapi import FastAPI


class UserData(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user": user_id}


@app.post("/details")
def get_user_details(user: UserData):
    return user
