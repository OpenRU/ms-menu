import requests
from flask import request

from app.config import MS_AUTH_PREFIX


def is_authenticated():
    token = request.headers.get("Authorization")

    if token is None:
        return False

    try:
        endpoint = f"{MS_AUTH_PREFIX}/validate-token"
        response = requests.post(endpoint, {'token': token})
        return response.status_code == 200
    except requests.RequestException:
        return False
