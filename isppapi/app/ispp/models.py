from app.db import db, BaseModelMixin


class Carrera(db.Model, BaseModelMixin):
    CarreraID = db.Column(db.Integer, primary_key=True)
    CarreraNombre = db.Column(db.String(255))
    Carpos = db.relationship('carpo', backref='carrera',
                             lazy=False, cascade='all, delete-orphan')

    def __init__(self, CarreraID, CarreraNombre, Carpos):
        self.CarreraID = CarreraID
        self.CarreraNombre = CarreraNombre
        self.Carpos = Carpos


class Plan(db.Model, BaseModelMixin):
    PlanID = db.Column(db.Integer, primary_key=True)
    PlanNombre = db.Column(db.String(255))
    Carpos = db.relationship('carpo', backref='plan',
                             lazy=False, cascade='all, delete-orphan')

    def __init__(self, PlanID, PlanNombre, Carpos):
        self.PlanID = PlanID
        self.PlanNombre = PlanNombre
        self.Carpos = Carpos


class Orientacion(db.Model, BaseModelMixin):
    OrientacionID = db.Column(db.Integer, primary_key=True)
    OrientacionNombre = db.Column(db.String(255))
    Carpos = db.relationship(
        'carpo', backref='orientacion', lazy=False, cascade='all, delete-orphan')

    def __init__(self, OrientacionID, OrientacionNombre, Carpos):
        self.OrientacionID = OrientacionID
        self.OrientacionNombre = OrientacionNombre
        self.Carpos = Carpos


class Carpo(db.Model, BaseModelMixin):
    CARPOID = db.Column(db.Integer, primary_key=True)
    CarreraID = db.Column(db.Integer, db.ForeignKey('carrera.carreraid'))
    PlanDeEstudioID = db.Column(db.Integer, db.ForeignKey('plan.planid'))
    OrientacionID = db.Column(
        db.Integer, db.ForeignKey('orientacion.orientacionid'))
    CarpoPrograma = db.Column(db.String(255))
    Materias = db.relationship(
        'materia', backref='carpo', lazy=False, cascade='all, delete-orphan')

    def __init__(self, CARPOID, CarreraID, PlanDeEstudioID, OrientacionID, Materias):
        self.CARPOID = CARPOID
        self.CarreraID = CarreraID
        self.PlanDeEstudioID = PlanDeEstudioID
        self.CarpoPrograma = CarpoPrograma
        self.Materias = Materias


class Materia(db.Model, BaseModelMixin):
    MateriaID = db.Column(db.Integer, primary_key=True)
    MateriaNombre = db.Column(db.String(255))
    MateriaAño = db.Column(db.String(255))
    MateriaTipo = db.Column(db.String(255))
    CarpoIDMat = db.Column(db.Integer, db.ForeignKey(
        'carpo.carpoid'), nullable=False)

    def __init__(self, MateriaID, MateriaNombre, MateriaAño, MateriaTipo, CarpoIDMat):
        self.MateriaID = MateriaID
        self.MateriaNombre = MateriaNombre
        self.MateriaAño = MateriaAño
        self.MateriaTipo = MateriaTipo
        self.CarpoIDMat = CarpoIDMat
