from typing import Optional
import datetime

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
import logging
from dotenv import load_dotenv

import main

load_dotenv()

# Configure the logging settings
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
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
    # backlog = relationship(ActivitiesBacklog.__tablename__, backref=__tablename__)


class ActivityVersion(Base):
    __tablename__ = 'Activity_versions'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    Activity_data_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Activity_data.id'))
    # backlog = relationship(ActivitiesBacklog.__tablename__, backref=__tablename__)


class Activity(Base):
    __tablename__ = 'Activity_data'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    # ActivityVersions = relationship("Activity_versions", backref=__tablename__)
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
    # Activity = relationship(Activity.__tablename__, backref=__tablename__)


class Type(Base):
    __tablename__ = 'type'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    region_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    # Activity = relationship(Activity.__tablename__, backref=__tablename__)


class Translation(Base):
    __tablename__ = 'translation'
    text_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("text.id"), primary_key=True, nullable=False)
    language_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("language.id"), primary_key=True,
                                    nullable=False)
    text = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)


class Language(Base):
    __tablename__ = 'language'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    language_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    # transl = relationship(Translation.__tablename__, backref=__tablename__)


class Text(Base):
    __tablename__ = 'text'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    # transl = relationship(Translation.__tablename__, backref=__tablename__)


# TODO: add more fields as they are added to the db

class User(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    # Activity = relationship(Activity.__tablename__, backref=__tablename__)


class Images(Base):
    __tablename__ = 'images'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    file_path = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    numberElements = sqlalchemy.Column(sqlalchemy.Integer)
    # Activity = relationship(Activity.__tablename__, backref=__tablename__)


class database:
    engine = None
    Session = None
    languages = None

    def __init__(self):
        # Define the MariaDB engine using MariaDB Connector/Python
        engine = sqlalchemy.create_engine(
            f"mariadb+mariadbconnector://{os.environ['SQL_LOGIN']}:{os.environ['SQL_PASSWORD']}@127.0.0.1:3306/mydb")
        try:
            with engine.connect():
                logging.info("maria db connected  successfully!")
        except SQLAlchemyError as e:
            logging.critical("Failed to create engine:", str(e))

        self.Session = sqlalchemy.orm.sessionmaker()
        self.Session.configure(bind=engine)
        self.Session = self.Session()
        ##pull the languages dict
        self.get_languages()

    def get_languages(self):
        query = self.Session.query(Language).all()
        self.languages = {row.language_name: row.id for row in query}


def get_region_id(db: database, activity: main.Activity):
    # hard coded 1 for guam for now
    return 1


def get_type_id(db: database, activity: main.Activity):
    # hard coded 0 for now
    return 0


def get_author_id(db: database, activity: main.Activity):
    # hard coded 0 for admin for now
    return 0


def save_img_path(db: database, activity: main.Activity):
    images = Images(file_path=activity.image_link, numberElements=1)
    db.Session.add(images)
    db.Session.commit()
    return images.id


def insert_text(db: database, text_str: str, lang_pref: str):
    text = Text()
    db.Session.add(text)
    db.Session.commit()
    translation = Translation(text_id=text.id, language_id=db.languages[lang_pref], text=text_str)
    db.Session.add(translation)
    db.Session.commit()
    return text.id


def insert_activity(db: database, activity: main.Activity):
    name_id: int = insert_text(db=db, text_str=activity.name, lang_pref=activity.lang_pref)
    description_id: int = insert_text(db=db, text_str=activity.description, lang_pref=activity.lang_pref)
    short_descr_id: int = insert_text(db=db, text_str=activity.short_description, lang_pref=activity.lang_pref)
    region_id: int = get_region_id(db=db, activity=activity)
    type_id: int = get_type_id(db=db, activity=activity)
    images_id: int = save_img_path(db=db, activity=activity)
    author_id: int = get_author_id(db=db, activity=activity)

    db_activity: Activity = Activity(Region_id=region_id, description_id=description_id, name_id=name_id,
                                     shortDescrip_id=short_descr_id, type_id=type_id, images_id=images_id
                                     , author_id=author_id)
    db.Session.add(db_activity)
    db.Session.commit()

