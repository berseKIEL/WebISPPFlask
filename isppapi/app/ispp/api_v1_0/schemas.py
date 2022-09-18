from marshmallow import fields

from app.ext import ma


class Usuario(ma.Schema):
    idusuario = fields.Integer(dump_only=True)
    usuario = fields.String()
    contraseña = fields.String()
    email = fields.String()
    contraseñatemp = fields.String()


class Perfiles(db.Model, BaseModelMixin):
    idperfiles = fields.Integer(dump_only=True)
    perfil = fields.String()


class UsuariosPerfiles(db.Model, BaseModelMixin):
    idusuarioperfil = fields.Integer(dump_only=True)
    idusuario = fields.Integer()
    idperfil = fields.Integer()


class Estudiante(db.Model, BaseModelMixin):
    idestudiante = fields.Integer(dump_only=True)
    NombreAlumno = fields.String()
    ApellidoAlumno = fields.String()
    DNI = fields.Integer()


class Carpo(db.Model, BaseModelMixin):
    CARPOID = fields.Integer(dump_only=True)
    CarreraID = fields.Integer()
    PlanDeEstudioID = fields.Integer()
    OrientacionID = fields.Integer()
    contraseñatemp = fields.String()


class Materia(db.Model, BaseModelMixin):
    idmateria = fields.Integer(dump_only=True)
    nombremateria = fields.String()
    año = fields.String()
    tipo = fields.String()


class CarpoEstudiante(db.Model, BaseModelMixin):
    idCARPOEstudiante = fields.Integer(dump_only=True)
    idCARPO = fields.Integer()
    contraseña = fields.String()


class Bedel(db.Model, BaseModelMixin):
    idbedel = fields.Integer(dump_only=True)
    nombrebedel = fields.String()


class Profesor(db.Model, BaseModelMixin):
    idprofesor = fields.Integer(dump_only=True)
    nombreprofesor = fields.String()
