from flask import Blueprint
from controllers.serieController import get_series


series_route = Blueprint('series_route', __name__)
series_route.route('/', methods=['GET'])(get_series)