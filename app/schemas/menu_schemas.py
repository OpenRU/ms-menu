from marshmallow import validate

from app.extensions import ma
from app.models import Menu


class MenuInSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Menu
        load_instance = True

    date = ma.Date(required=True)
    main_dish = ma.String(required=True, validate=validate.Length(min=1, max=255))
    side_dish = ma.String(required=True, validate=validate.Length(min=1, max=255))
    salad = ma.String(required=True, validate=validate.Length(min=1, max=255))
    dessert = ma.String(required=True, validate=validate.Length(min=1, max=255))
    drink = ma.String(required=True, validate=validate.Length(min=1, max=255))


class MenuPutSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Menu

    date = ma.Date(required=True)
    main_dish = ma.String(required=True, validate=validate.Length(min=1, max=255))
    side_dish = ma.String(required=True, validate=validate.Length(min=1, max=255))
    salad = ma.String(required=True, validate=validate.Length(min=1, max=255))
    dessert = ma.String(required=True, validate=validate.Length(min=1, max=255))
    drink = ma.String(required=True, validate=validate.Length(min=1, max=255))


class MenuOutSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Menu
        load_instance = True

    id = ma.Integer(dump_only=True)
    date = ma.Date()
    main_dish = ma.String()
    side_dish = ma.String()
    salad = ma.String()
    dessert = ma.String()
    drink = ma.String()
