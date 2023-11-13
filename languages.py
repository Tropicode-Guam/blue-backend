from iso639.iso639 import Iso639
from dotenv import load_dotenv
import database as db
languages = Iso639()
load_dotenv()
for language in languages:
    # Access the ISO 639-1 code and language name
    iso_639_1 = language.alpha2
    language_name = language.name
    database = db.database()
    # Print the language code and name
    if iso_639_1:
        database.Session.add(db.Language(language_name=iso_639_1))

    database.Session.commit()

