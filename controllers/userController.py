# coding: utf-8
from flask import request
import requests

def user_sub(func):
    def decorateur(*args, **kwargs):
        try:
            r = requests.get(f'http://127.0.0.1:5001/users/{request.headers.get("idUser")}')
            if r.json()['status'] == 'on':
                resultat = func(*args, **kwargs)
            else:
                resultat = "400"
            return resultat
        except Exception:
            return "500"
    return decorateur