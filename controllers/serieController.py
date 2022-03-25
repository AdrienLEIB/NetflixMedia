from flask import request, jsonify
from models.Serie import Serie
from models.Episode import Episode

def get_series():
    films = Serie.objects()
    return jsonify(films), 200

def get_serie(id):
    return jsonify(Serie.objects.get_or_404(id=id)), 200

def create_serie():
    body = request.get_json()
    serie = Serie(**body).save()
    return jsonify(serie), 201

def update_serie(id):
    body = request.get_json()
    serie = Serie.objects.get_or_404(id=id)
    serie.update(**body)
    return jsonify(Serie.objects.get_or_404(id=id)), 201

def delete_serie(id):
    serie = Serie.objects.get_or_404(id=id)
    for idEpisode in serie.episodes:
        episode = Episode.objects.get_or_404(id=idEpisode)
        episode.delete()
    Serie.delete()
    return jsonify(str(serie.id)), 200
