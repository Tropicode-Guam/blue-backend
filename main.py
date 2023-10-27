from __future__ import annotations
import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel


class Activity(BaseModel):
    name: str
    description: str
    short_description: str
    image_link: str
    lat: float = None
    lon: float = None
    gmap_link: str
    lang_pref: str = 'en'
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
    redirect: str = await get_redirect(place.gmap_link)
    coordinates = redirect.split('@')[1].split(',')[:2]
    latitude: float = float(coordinates[0])
    longtitude: float = float(coordinates[1])

    return place


async def get_redirect(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return str(response.url)
