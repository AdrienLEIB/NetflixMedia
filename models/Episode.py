from flask_mongoengine import MongoEngine
db = MongoEngine()


class Episode(db.Document):
    number = db.IntField()
    serie = db.StringField()
    url =  db.URLField()
    idSerie = db.StringField()

