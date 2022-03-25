from flask import Flask
from flask_mongoengine import MongoEngine
from routes.serieRoute import series_route
from routes.filmRoute import films_route
from routes.episodeRoute import episodes_route
from  routes.swaggerRoute import swagger_route


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(episodes_route, url_prefix='/episodes')
app.register_blueprint(series_route, url_prefix='/series')
app.register_blueprint(films_route, url_prefix='/films')
app.register_blueprint(swagger_route)
db = MongoEngine()
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
