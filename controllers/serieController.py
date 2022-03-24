
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Serie import Serie
import uuid

def get_series():
    series = Serie.objects()
    return jsonify(series), 200
