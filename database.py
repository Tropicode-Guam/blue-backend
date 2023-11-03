from typing import Optional
import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = None

Base = declarative_base()


class ActivitiesBacklog(Base):
    __tablename__ = 'activities_backlog'
    Activities_GIS_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Activities_GIS.id'),
                                          primary_key=True, nullable=False)
    Activity_versions_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Activity_versions.id'),
                                             primary_key=True, nullable=False)
    timestamp = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=False)


class ActivitiesGIS(Base):
    __tablename__ = 'Activities_GIS'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    x_coordinate = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    y_coordinate = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    backlog = relationship(ActivitiesBacklog.__tablename__, backref=__tablename__)


class ActivityVersion(Base):
    __tablename__ = 'Activity_versions'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    Activity_data_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Activity_data.id'))
    backlog = relationship(ActivitiesBacklog.__tablename__, backref=__tablename__)


class Activity(Base):
    __tablename__ = 'Activity_data'
    ActivityVersions = relationship("Activity_versions", backref=__tablename__)
    Region_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Region'))
    description_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("text"))
    name_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("text"))
    shortDescrip_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("text"))
    type_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("type"))
    images_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("images"))
    author_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user"))


class Region(Base):
    __tablename__ = 'Region'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    region_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    Activity = relationship(Activity.__tablename__, backref=__tablename__)


class Type(Base):
    __tablename__ = 'type'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    region_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    Activity = relationship(Activity.__tablename__, backref=__tablename__)


class Language(Base):
    __tablename__ = 'language'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    region_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    Translation = relationship(Translation.__tablename__, backref=__tablename__)


class Text(Base):
    __tablename__ = 'text'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    Translation = relationship(Translation.__tablename__, backref=__tablename__)


class Translation(Base):
    __tablename__ = 'translation'
    text_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("text"), primary_key=True, nullable=False)
    language_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("language"), primary_key=True,
                                    nullable=False)
    text = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)


# TODO: add more fields as they are added to the db

class User(Base):
    __tablename__ = 'translation'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    Activity = relationship(Activity.__tablename__, backref=__tablename__)


class Images(Base):
    __tablename__ = 'images'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    file_path = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    numberElements = sqlalchemy.Column(sqlalchemy.Integer)
    Activity = relationship(Activity.__tablename__, backref=__tablename__)
