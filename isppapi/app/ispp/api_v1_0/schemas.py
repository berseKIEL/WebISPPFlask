from marshmallow import fields

from app.ext import ma


class CarreraSchema(ma.Schema):
    CarreraID = fields.Integer(dump_only=True)
    CarreraNombre = fields.String()


class PlanSchema(ma.Schema):
    PlanID = fields.Integer(dump_only=True)
    PlanNombre = fields.String()


class OrientacionSchema(ma.Schema):
    OrientacionID = fields.Integer(dump_only=True)
    OrientacionNombre = fields.String()


class CarpoSchema(ma.Schema):
    CARPOID = fields.Integer(dump_only=True)
    CarpoPrograma = fields.String()


class MateriaSchema(ma.Schema):
    MateriaID = fields.Integer(dump_only=True)
    MateriaNombre = fields.String()
    MateriaAño = fields.String()
    MateriaTipo = fields.String()
