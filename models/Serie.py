from flask_mongoengine import MongoEngine
db = MongoEngine()


class Serie(db.Document):
    title = db.StringField()
    description = db.StringField()
    episodes = db.ListField(db.StringField())
    categorie = db.StringField()
    img = db.URLField()
    localisation = db.StringField()

