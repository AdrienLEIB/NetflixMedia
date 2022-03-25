
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Serie import Serie
import uuid

def get_series():
    series = Serie.objects()
    return jsonify(series), 200



def create_serie():

    request_data = request.get_json()
    Serie.save(request_data)
    return jsonify(), 201
