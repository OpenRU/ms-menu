import os

from flask import Flask
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException, NotFound


def create_app(env: str = None) -> Flask:
    app = Flask(__name__)
    from . import config

    match env or os.getenv("ENV", default="PRODUCTION"):
        case "PRODUCTION":
            app.config.from_object(config.ProductionSettings)
        case "DEVELOPMENT":
            app.config.from_object(config.DevelopmentSettings)
        case _:
            raise RuntimeError(f"Ambiente de execução '{env}' não reconhecido")

    from app.extensions import db, migrate, ma, api
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    api.init_app(app)

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        return {"description": "Erro de validação", "errors": error.messages}, 422

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        return {"description": "Recurso não encontrado"}, error.code

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return {"description": "Erro HTTP inesperado"}, error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        print(error)
        return {"description": "Erro interno no servidor"}, 500

    from app import models
    from app import schemas

    from app.routes import menu_blp
    api.register_blueprint(menu_blp)

    return app
