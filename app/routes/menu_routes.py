from datetime import date
from typing import Any

from flask_smorest import Blueprint
from flask_smorest import abort

from app.auth import is_authenticated
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
    if not is_authenticated():
        abort(401, message="O token não foi enviando ou é inválido")

    stmt = db.select(Menu).where(Menu.date == menu.date).limit(1)
    if db.session.scalars(stmt).first():
        abort(409, message="Já existe um menu cadastrado para esta data")

    db.session.add(menu)
    db.session.commit()
    return menu


@menu_blp.route("/<int:menu_id>", methods=["PUT"])
@menu_blp.arguments(MenuPutSchema)
@menu_blp.response(200, MenuOutSchema)
@menu_blp.alt_response(404)
def update_menu(menu_data: dict[str, Any], menu_id: int):
    if not is_authenticated():
        abort(401, message="O token não foi enviando ou é inválido")

    stmt = db.select(Menu).where(Menu.date == menu_data["date"], Menu.id != menu_id).limit(1)
    if db.session.scalars(stmt).first():
        abort(409, message="Já existe um menu cadastrado para esta data")

    menu = db.get_or_404(Menu, menu_id)
    for key, value in menu_data.items():
        setattr(menu, key, value)

    db.session.commit()
    return menu


@menu_blp.route("/<int:menu_id>", methods=["DELETE"])
@menu_blp.response(204)
def delete_menu(menu_id: int):
    if not is_authenticated():
        abort(401, message="O token não foi enviando ou é inválido")

    menu = db.get_or_404(Menu, menu_id)
    db.session.delete(menu)
    db.session.commit()


@menu_blp.route("/today", methods=["GET"])
@menu_blp.response(200, MenuOutSchema)
@menu_blp.alt_response(404)
def get_today_menu():
    today = date.today()
    stmt = db.select(Menu).where(Menu.date == today).limit(1)
    menu = db.session.scalars(stmt).first()
    if menu is None:
        abort(404, message="Nenhum cardápio encontrado para hoje")

    return menu
