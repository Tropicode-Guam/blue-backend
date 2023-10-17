from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel


class Activity(BaseModel):
    name: str
    description: str
    short_description: str
    image_link: str
    lat: float
    lon: float
    lang_pref: int = 0
    author: int = 0


app = FastAPI()


@app.get("/places")
async def root():
    return {"message": "Hello, World!"}


@app.get("/places/{id}")
async def get_activity_data(id: int, lang_pref: int = 0):
    return {"id": id}


@app.post("/place")
async def add_place(place: Activity):
    return place
