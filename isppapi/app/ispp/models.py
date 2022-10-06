from app.db import db, BaseModelMixin


class Carrera(db.Model, BaseModelMixin):
    CarreraID = db.Column(db.Integer, primary_key=True)
    CarreraNombre = db.Column(db.String(255))
    Carpos = db.relationship('Carpo', backref='carrera')

    def __init__(self, CarreraNombre):
        self.CarreraNombre = CarreraNombre


class Plan(db.Model, BaseModelMixin):
    PlanID = db.Column(db.Integer, primary_key=True)
    PlanNombre = db.Column(db.String(255))
    Carpos = db.relationship('Carpo', backref='plan')

    def __init__(self, PlanNombre):
        self.PlanNombre = PlanNombre


class Orientacion(db.Model, BaseModelMixin):
    OrientacionID = db.Column(db.Integer, primary_key=True)
    OrientacionNombre = db.Column(db.String(255))
    Carpos = db.relationship('Carpo', backref='orientacion')

    def __init__(self, OrientacionNombre):
        self.OrientacionNombre = OrientacionNombre


class Carpo(db.Model, BaseModelMixin):
    CarpoID = db.Column(db.Integer, primary_key=True)
    CarreraID = db.Column(db.Integer, db.ForeignKey(
        'carrera.CarreraID'), nullable=False)
    PlanDeEstudioID = db.Column(
        db.Integer, db.ForeignKey('plan.PlanID'), nullable=False)
    OrientacionID = db.Column(
        db.Integer, db.ForeignKey('orientacion.OrientacionID'))
    CarpoPrograma = db.Column(db.String(255))
    Materias = db.relationship('Materia', backref='carpo')

    def __init__(self, CarreraID, OrientacionID, PlanDeEstudioID):
        self.CarreraID = CarreraID
        self.OrientacionID = OrientacionID
        self.PlanDeEstudioID = PlanDeEstudioID


class Materia(db.Model, BaseModelMixin):
    MateriaID = db.Column(db.Integer, primary_key=True)
    MateriaNombre = db.Column(db.String(255))
    MateriaAño = db.Column(db.String(255))
    MateriaTipo = db.Column(db.String(255))
    CarpoIDMat = db.Column(db.Integer, db.ForeignKey(
        'carpo.CarpoID'), nullable=False)

    def __init__(self, MateriaNombre, CarpoIDMat):
        self.MateriaNombre = MateriaNombre
        self.CarpoIDMat = CarpoIDMat
