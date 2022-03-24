from flask import Flask
from routes.serieRoute import series_route


app = Flask(__name__)
app.config.from_object('config')


app.register_blueprint(series_route, url_prefix='/series')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
