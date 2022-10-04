from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import CarpoSchema, CarreraSchema, OrientacionSchema, PlanSchema, MateriaSchema
from ..models import Carrera, Plan, Orientacion, Carpo, Materia

carreras_v_1_0_bp = Blueprint('carreras', __name__)

carrera_schema = CarreraSchema()

api = Api(carreras_v_1_0_bp)

class CarrerasListaRecursos(Resource):
    def get(self):
        carreras = Carrera.get_all()
        resultado = carrera_schema.dump(carreras,many=True)
        return resultado

api.add_resource(CarrerasListaRecursos, '/api/v1.0/carreras', endpoint='carreras_lista_recursos')

# api.add_resource(CarrerasRecursos, 'api/v1.0/carreras/<int:carrera_id>', endpoint='carreras_recursos')