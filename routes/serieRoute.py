from flask import Blueprint
from controllers.serieController import getAll


series_route = Blueprint('series_route', __name__)
series_route.route('/', methods=['GET'])(getAll)