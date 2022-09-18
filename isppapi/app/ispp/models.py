from app.db import db, BaseModelMixin


class Usuario(db.Model, BaseModelMixin):
    idusuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(255))
    contraseña = db.Column(db.String(255))
    email = db.Column(db.String(255))
    contraseñatemp = db.Column(db.String(255))

    def __init__(self, idusuario, usuario, contraseña, email):
        self.idusuario = idusuario
        self.usuario = usuario
        self.contraseña = contraseña
        self.email = email

    def __repr__(self, idusuario):
        return f'{idusuario}'

    def __str__(self):
        return f'{usuario}'


class Perfil(db.Model, BaseModelMixin):
    idperfiles = db.Column(db.Integer, primary_key=True)
    perfil = db.Column(db.String(255))

    def __init__(self, idperfiles, perfil):
        self.idperfiles = idperfiles
        self.perfil = perfil

    def __repr__(self, idperfiles):
        return f'{idperfiles}'

    def __str__(self):
        return f'{idperfiles}'


class UsuariosPerfiles(db.Model, BaseModelMixin):
    idusuarioperfil = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer,db.ForeignKey('usuario.idusuario'), nullable=False)
    idperfil = db.Column(db.Integer,db.ForeignKey('perfiles.idperfiles'), nullable=False)

    def __init__(self, idusuarioperfil, idusuario, idperfil):
        self.idusuarioperfil = idusuario
        self.usuario = usuario
        self.idperfil = contraseña

    def __repr__(self, idusuarioperfil):
        return f'{idusuarioperfil}'


class Estudiante(db.Model, BaseModelMixin):
    idestudiante = db.Column(db.Integer, primary_key=True)
    NombreAlumno = db.Column(db.String(255))
    ApellidoAlumno = db.Column(db.String(255))
    DNI = db.Column(db.Integer)

    def __init__(self, idestudiante, NombreAlumno, ApellidoAlumno, DNI):
        self.idestudiante = idestudiante
        self.NombreAlumno = NombreAlumno
        self.ApellidoAlumno = ApellidoAlumno
        self.DNI = DNI

    def __repr__(self, idestudiante):
        return f'{idestudiante}'

    def __str__(self):
        return f'{NombreAlumno}'


class Carpo(db.Model, BaseModelMixin):
    CARPOID = db.Column(db.Integer, primary_key=True)
    CarreraID = db.Column(db.Integer)
    PlanDeEstudioID = db.Column(db.Integer)
    OrientacionID = db.Column(db.Integer)
    CarpoPrograma = db.Column(db.String(255))

    def __init__(self, CARPOID, CarreraID, PlanDeEstudioID, OrientacionID):
        self.CARPOID = CARPOID
        self.CarreraID = CarreraID
        self.PlanDeEstudioID = PlanDeEstudioID
        self.CarpoPrograma = CarpoPrograma

    def __repr__(self, CARPOID):
        return f'{CARPOID}'


class Materia(db.Model, BaseModelMixin):
    idmateria = db.Column(db.Integer, primary_key=True)
    nombremateria = db.Column(db.String(255))
    año = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
    carpo = db.Column(db.Integer,db.ForeignKey('carpo.carpoid'), nullable=False)

    def __init__(self, idmateria, nombremateria, año, tipo,carpo):
        self.idmateria = idmateria
        self.nombremateria = nombremateria
        self.año = año
        self.tipo = tipo
        self.carpo = carpo

    def __repr__(self, idmateria):
        return f'{idmateria}'

    def __str__(self):
        return f'{nombremateria}'


class CarpoEstudiante(db.Model, BaseModelMixin):
    idCARPOEstudiante = db.Column(db.Integer, primary_key=True)
    idCARPO = db.Column(db.Integer,db.ForeignKey('carpo.carpoid'),nullable=False)
    idEstudiante = db.Column(db.Integer,db.Integer,db.ForeignKey('carpo.carpoid'),nullable=False)

    def __init__(self, idCARPOEstudiante, idCARPO, idEstudiante):
        self.idCARPOEstudiante = idCARPOEstudiante
        self.idCARPO = idCARPO
        self.idEstudiante = idEstudiante

    def __repr__(self, idusuario):
        return f'{idCARPOEstudiante}'


class Bedel(db.Model, BaseModelMixin):
    idbedel = db.Column(db.Integer, primary_key=True)
    nombrebedel = db.Column(db.String(255))

    def __init__(self, idbedel, nombrebedel):
        self.idbedel = idbedel
        self.nombrebedel = nombrebedel

    def __repr__(self, idbedel):
        return f'{idbedel}'

    def __str__(self):
        return f'{nombrebedel}'


class Profesor(db.Model, BaseModelMixin):
    idprofesor = db.Column(db.Integer, primary_key=True)
    nombreprofesor = db.Column(db.String(255))

    def __init__(self, idprofesor, nombreprofesor):
        self.idprofesor = idprofesor
        self.nombreprofesor = nombreprofesor

    def __repr__(self, idprofesor):
        return f'{idprofesor}'

    def __str__(self):
        return f'{nombreprofesor}'
