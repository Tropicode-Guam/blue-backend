from databases import Database
from sqlalchemy import MetaData

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)
metadata = MetaData()

# Define your tables using SQLAlchemy ORM
from sqlalchemy import Table, Column, Integer, String

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("email", String(50)),
)

# Connect and disconnect to the database in event handlers
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Define your API routes
from pydantic import BaseModel

class UserIn(BaseModel):
    name: str
    email: str

class UserOut(UserIn):
    id: int

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}

@app.get("/users/", response_model=list[UserOut])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)
    
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

