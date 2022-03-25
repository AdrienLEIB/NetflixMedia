from flask import request, jsonify
from models.Episode import Episode
from models.Serie import Serie

def get_episodes():
    episodes = Episode.objects()
    return jsonify(episodes), 200

def get_episode(id):
    return jsonify(Episode.objects.get_or_404(id=id)), 200

def create_episode():
    return jsonify(Episode(**request.get_json()).save()), 201

def update_episode(id):
    body = request.get_json()
    episode = Episode.objects.get_or_404(id=id)
    episode.update(**body)
    if body["idSerie"]:
        serie = Serie.objects.get_or_404(id=id)
        if str(episode.id) not in serie.episodes:
            serie.episodes.append(str(episode.id))
            serie.update(serie)

    return jsonify(Episode.objects.get_or_404(id=id)), 201

def delete_episode(id):
    episode = Episode.objects.get_or_404(id=id)
    if episode.idSerie:
        serie = Serie.objects.get_or_404(id=episode.idSerie)
        serie.episodes.remove(str(episode.id))
        serie.update(serie)

    episode.delete()
    return jsonify(str(episode.id)), 200