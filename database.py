from typing import Optional
import datetime
from sqlmodel import Field, SQLModel


class ActivityGIS(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    x_coordinate: Optional[int]
    y_coordinate: Optional[int]


class ActivityData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    Region_id: int
    description_id: int
    name_id: int
    shortDescrip_id: int
    type_id: int
    images_id: int
    author_id: int


class activities_backlog(SQLModel, table=True):
    Activities_GIS_id: int
    Activity_versions_id: int
    timestamp: datetime


class Activity_versions(SQLModel, table=True):
    id: int
    Activity_data_id: int


class type(SQLModel, table=True):
    id: int
    name: str


class Region(SQLModel, table=True):
    id: int
    region_name: str


class user(SQLModel, table=True):
    id: int


class text(SQLModel, table=True):
    id: int


class language(SQLModel, table=True):
    id: int
    language_name: str


class translation(SQLModel, table=True):
    text_id: int
    language_id: int
    text: str

