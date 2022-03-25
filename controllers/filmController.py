from flask import request, jsonify
from models.Film import Film

def get_films():
    films = Film.objects()
    return jsonify(films), 200

def get_film(id):
    return jsonify(Film.objects.get_or_404(id=id)), 200

def create_film():
    body = request.get_json()
    film = Film(**body).save()
    return jsonify(film), 201

def update_film(id):
    body = request.get_json()
    film = Film.objects.get_or_404(id=id)
    film.update(**body)
    return jsonify(Film.objects.get_or_404(id=id)), 201

def delete_film(id):
    film = Film.objects.get_or_404(id=id)
    film.delete()
    return jsonify(str(film.id)), 200