from flask_mongoengine import MongoEngine
db = MongoEngine()

class Film(db.Document):

    title = db.StringField()
    url = db.StringField()
    categorie = db.StringField()
    description = db.StringField()


    def __init__(self, name):
        self._name = name

