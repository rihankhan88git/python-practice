from fastapi import FastAPI
from pydantic import BaseModel, Field
import db


app = FastAPI()


# CREATE TABLE WHEN SERVER STARTS
@app.on_event("startup")
def startup():
    db.create_table()


# USER MODEL
class User(BaseModel):
    name: str=Field(...,min_length=3,max_length=20)
    address: str=Field(...,min_length=8,max_length=50)
    course: str=Field(...,min_length=4,max_length=20)
    fee: float=Field(...,gt=0)
    email: str=Field(...,min_length=10,max_length=50)


# CREATE USER
@app.post("/users", status_code=201)
def create_user(user: User):
    return db.create_user(user)


# GET ALL USERS
@app.get("/users")
def get_all_users():
    return db.get_users()


# GET USER BY IDs
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return db.get_user_by_id(user_id)


# UPDATE USER
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return db.update_user(user_id, user)


# DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return db.delete_user(user_id)