from __future__ import annotations
import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel
import logging
import api.database as db
import os
from dotenv import load_dotenv

load_dotenv()
API_BASE_PATH = os.environ['VIRTUAL_PATH']
# Configure the logging settings
logging.basicConfig(filename='blue_backend.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
database: db.database = db.database()


class Place(BaseModel):
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


@app.get(API_BASE_PATH + "/places")
async def root():
    return [{
		'id': 0,
		'title': "Pagat Caves",
		'desc': "Enjoy this 2.7-km out-and-back trail near Yigo. Generally considered a moderately challenging route, it takes an average of 1 h 4 min to complete. This is a very popular area for hiking, so you'll likely encounter other people while exploring. The trail is open year-round and is beautiful to visit anytime.",
		'pos': [13.49995, 144.87714],
		'type': "hike",
		'state': "Guam",
		'img': "https://res.klook.com/images/fl_lossy.progressive,q_65/c_fill,w_1295,h_777/w_80,x_15,y_15,g_south_west,l_Klook_water_br_trans_yhcmh3/activities/peh07lgpjbxzdmzoz34i/PagatCavesTrekkingExperienceinGuam.webp",
	}]


@app.get(API_BASE_PATH + "/places/{id}")
async def get_activity_data(id: int, lang_pref: int = 0):
    return 	{
		'id': 0,
		'title': "Pagat Caves",
		'desc': "Enjoy this 2.7-km out-and-back trail near Yigo. Generally considered a moderately challenging route, it takes an average of 1 h 4 min to complete. This is a very popular area for hiking, so you'll likely encounter other people while exploring. The trail is open year-round and is beautiful to visit anytime.",
		'pos': [13.49995, 144.87714],
		'type': "hike",
		'state': "Guam",
		'img': "https://res.klook.com/images/fl_lossy.progressive,q_65/c_fill,w_1295,h_777/w_80,x_15,y_15,g_south_west,l_Klook_water_br_trans_yhcmh3/activities/peh07lgpjbxzdmzoz34i/PagatCavesTrekkingExperienceinGuam.webp",
	}


@app.post(API_BASE_PATH + "/place")
async def add_place(place: Place):
    logging.debug("Post request received")
    redirect: str = await get_redirect(place.gmap_link)
    coordinates = redirect.split('@')[1].split(',')[:2]
    place.lat = float(coordinates[0])
    place.lon = float(coordinates[1])

    db.insert_activity(database, place)
    return place


async def get_redirect(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return str(response.url)
