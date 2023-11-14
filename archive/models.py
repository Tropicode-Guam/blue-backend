from pydantic import BaseModel, constr, validator
from typing import List, Optional
from datetime import time, date

class Location(BaseModel):
    google_maps_link: str
    latitude: float
    longitude: float

    @validator("google_maps_link")
    def validate_google_maps_link(cls, v):
        if "google.com/maps" not in v:
            raise ValueError("Invalid Google Maps link")
        return v

class TimeInfo(BaseModel):
    days: List[date]
    start_time: time
    end_time: time
    recurring: bool

class Author(BaseModel):
    name: str
    phone_number: str  # We'll validate this with a separate function

    @validator('phone_number')
    def validate_phone_number(cls, phone_number):
        pattern = r"^\+?(\d[\d\-]{7,}\d)$"
        if not re.match(pattern, phone_number):
            raise ValueError(f"Invalid phone number format: {phone_number}")
        return phone_number

class Post(BaseModel):
    activity_title: str
    description: Optional[str]
    location: Location
    time_info: TimeInfo
    author: Author
