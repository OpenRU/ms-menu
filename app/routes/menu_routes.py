from datetime import datetime
from typing import Any

from flask_smorest import Blueprint

from app.extensions import db
from app.models import Menu
from app.schemas import MenuInSchema, MenuPutSchema, MenuOutSchema

menu_blp = Blueprint("menus", "menus", url_prefix="/menus", description="CRUD de cardápios")


@menu_blp.route("/<int:menu_id>", methods=["GET"])
@menu_blp.response(200, MenuOutSchema)
@menu_blp.alt_response(404)
def get_menu(menu_id: int):
    return db.get_or_404(Menu, menu_id)


@menu_blp.route("/", methods=["GET"])
@menu_blp.response(200, MenuOutSchema(many=True))
def list_menus():
    return db.session.scalars(db.select(Menu)).all()


@menu_blp.route("/", methods=["POST"])
@menu_blp.arguments(MenuInSchema)
@menu_blp.response(201, MenuOutSchema)
def create_menu(menu: Menu):
    # TODO: Checar se já tem um menu cadastrado na data enviada (menu.date)
    # Deve ser feita uma query e se o resultado não for nulo, jogue 409 conflict
    db.session.add(menu)
    db.session.commit()
    return menu


@menu_blp.route("/<int:menu_id>", methods=["PUT"])
@menu_blp.arguments(MenuPutSchema)
@menu_blp.response(200, MenuOutSchema)
@menu_blp.alt_response(404)
def update_menu(menu_data: dict[str, Any], menu_id: int):
    # TODO: Checar se já tem um menu cadastrado na data enviada atualizada (menu.date)
    # Deve ser feita uma query e se o resultado não for nulo, jogue 409 conflict
    menu = db.get_or_404(Menu, menu_id)
    for key, value in menu_data.items():
        setattr(menu, key, value)

    db.session.commit()
    return menu


@menu_blp.route("/<int:menu_id>", methods=["DELETE"])
@menu_blp.response(204)
def delete_menu(menu_id: int):
    menu = db.get_or_404(Menu, menu_id)
    db.session.delete(menu)
    db.session.commit()


@menu_blp.route("/now", methods=["GET"])
@menu_blp.response(200, MenuOutSchema)
@menu_blp.alt_response(404)
def get_today_menu():
    # TODO: Deve fazer uma query para um cardápio cadastrado na data atual e retorna 200 OK
    # Caso contrario deve retornar 404 NOT FOUND
    pass
