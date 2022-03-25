from flask_mongoengine import MongoEngine
import uuid
db = MongoEngine()

class Film(db.Document):
    title = db.StringField()
    url = db.URLField()
    categorie = db.StringField()
    description = db.StringField()

