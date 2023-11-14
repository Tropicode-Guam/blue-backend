from sqlalchemy import create_engine
from main import metadata, DATABASE_URL  # import metadata and DATABASE_URL

# Change the dialect to a synchronous one, e.g., pymysql or mysqlclient
# Assuming DATABASE_URL is in the format: mysql+aiomysql://<username>:<password>@<host>/<dbname>
sync_DATABASE_URL = DATABASE_URL.replace("aiomysql", "pymysql")

engine = create_engine(sync_DATABASE_URL)
metadata.create_all(engine)
