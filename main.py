from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel


class Activity(BaseModel):
    name: str
    description: str
    short_description: str
    image_link: str
    x_coordinate: float
    y_coordinate: float
    lang_pref: int | None = None


app = FastAPI()


@app.get("/places")
async def root():
    return {"message": "Hello, World!"}


@app.get("/places/{id}")
async def get_activity_data(id: int, lang_pref: int = 0):
    return {"id": id}
