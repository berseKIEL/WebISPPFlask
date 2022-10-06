from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import CarpoSchema, CarreraSchema, OrientacionSchema, PlanSchema, MateriaSchema
from ..models import Carrera, Plan, Orientacion, Carpo, Materia

carreras_v_1_0_bp = Blueprint('carreras_v_1_0_bp', __name__)

carrera_schema = CarreraSchema()

api = Api(carreras_v_1_0_bp)

class CarrerasListaRecursos(Resource):
    def get(self):
        carreras = Carrera.get_all()
        resultado = carrera_schema.dump(carreras,many=True)
        return resultado
    
    def post(self):
        data = request.get_json()
        print(data)
        carrera_dict = carrera_schema.load(data)
        carrera = Carrera(CarreraNombre=carrera_dict['CarreraNombre'])
        carrera.save()
        resp = carrera_schema.dump(carrera)
        return resp, 201
    
class CarrerasRecursos(Resource):
    def get(self, carrera_id):
        carrera = Carrera.get_by_id(carrera_id)
        if carrera is None:
            raise ObjectNotFound('La carrera no existe')
        resp = carrera_schema.dump(carrera)
        return resp


api.add_resource(CarrerasListaRecursos, '/api/v1.0/carreras/', endpoint='film_list_resource')
    
api.add_resource(CarrerasRecursos, '/api/v1.0/carreras/<int:carrera_id>', endpoint='carreras_recursos')