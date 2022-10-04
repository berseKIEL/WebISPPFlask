from marshmallow import fields

from app.ext import ma


class CarreraSchema(ma.Schema):
    CarreraID = fields.Integer(dump_only=True)
    CarreraNombre = fields.String()
    Carpos = fields.Nested('CarpoSchema', many=True)


class PlanSchema(ma.Schema):
    PlanID = fields.Integer(dump_only=True)
    PlanNombre = fields.String()
    Carpos = fields.Nested('CarpoSchema', many=True)


class OrientacionSchema(ma.Schema):
    OrientacionID = fields.Integer(dump_only=True)
    OrientacionNombre = fields.String()
    Carpos = fields.Nested('CarpoSchema', many=True)


class CarpoSchema(ma.Schema):
    CARPOID = fields.Integer(dump_only=True)
    CarpoPrograma = fields.String()
    Materias = fields.Nested('MateriaSchema', many=True)


class MateriaSchema(ma.Schema):
    MateriaID = fields.Integer(dump_only=True)
    MateriaNombre = fields.String()
    MateriaAño = fields.String()
    MateriaTipo = fields.String()
