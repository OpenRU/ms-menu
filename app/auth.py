import logging

import requests
from flask import request

from app.config import AUTH_URI

log = logging.getLogger(__name__)


def is_authenticated():
    if AUTH_URI is None or not AUTH_URI.strip():
        log.error("ERROR: A variável de ambiente AUTH_URI não foi definida")
        return True

    token = request.headers.get("Authorization")

    if token is None:
        log.warning("WARNING: Token não encontrado no Header Authorization")
        return False

    try:
        endpoint = f"{AUTH_URI}/auth/validate-token/"
        response = requests.get(endpoint, headers={"Authorization": token})
        print(response.request.headers)

        if response.status_code == 200:
            return True
        if response.status_code == 401:
            return False

        log.warning(f"WARNING: Código HTTP não documentado em response da API de autenticação: {response.status_code}")
        return False

    except requests.RequestException as exc:
        log.exception(f"EXCEPTION: Erro durante a validação do token: {exc}")
        return False
