from flask import request, Blueprint
from flask_restful import Api, Resource

from app.common.error_handling import ObjectNotFound

from .schemas import CarpoSchema, CarreraSchema, OrientacionSchema, PlanSchema, MateriaSchema
from ..models import Carrera, Plan, Orientacion, Carpo, Materia

carreras_v_1_0_bp = Blueprint('carreras_v_1_0_bp', __name__)

carrera_schema = CarreraSchema()
plan_schema = PlanSchema()
orientacion_schema = OrientacionSchema()

carpo_schema = CarpoSchema()

materia_schemas = MateriaSchema()

api = Api(carreras_v_1_0_bp)


class CarrerasListaRecursos(Resource):
    def get(self):
        carreras = Carrera.get_all()
        resultado = carrera_schema.dump(carreras, many=True)
        return resultado

    def post(self):
        data = request.get_json()
        carrera_dict = carrera_schema.load(data)
        carrera = Carrera(CarreraNombre=carrera_dict['CarreraNombre'])
        carrera.save()
        resp = carrera_schema.dump(carrera)
        return resp, 201


class CarrerasRecursos(Resource):
    def get(self, carrera_id):
        carrera = Carrera.get_by_id(carrera_id)
        if carrera is None:
            raise ObjectNotFound('La carrera solicitada no existe')
        resp = carrera_schema.dump(carrera)
        return resp


class PlanesListaRecursos(Resource):
    def get(self):
        planes = Plan.get_all()
        resultado = plan_schema.dump(planes, many=True)
        return resultado

    def post(self):
        data = request.get_json()
        plan_dict = plan_schema.load(data)
        plan = Plan(PlanNombre=plan_dict['PlanNombre'])
        plan.save()
        resp = plan_schema.dump(plan)
        return resp, 201


class PlanesRecursos(Resource):
    def get(self, plan_id):
        plan = Plan.get_by_id(plan_id)
        if plan is None:
            raise ObjectNotFound(f'El plan solicitado no existe')
        resp = plan_schema.dump(plan)
        return resp


class OrientacionesListaRecursos(Resource):
    def get(self):
        orientaciones = Orientacion.get_all()
        resultado = orientacion_schema.dump(orientaciones, many=True)
        return resultado

    def post(self):
        data = request.get_json()
        orientacion_dict = orientacion_schema.load(data)
        orientacion = Orientacion(
            OrientacionNombre=orientacion_dict['OrientacionNombre'])
        orientacion.save()
        resp = orientacion_schema.dump(orientacion)
        return resp, 201


class OrientacionesRecursos(Resource):
    def get(self, orientacion_id):
        orientacion = Orientacion.get_by_id(orientacion_id)
        if orientacion is None:
            raise ObjectNotFound('La Orientacion solicitada no existe')
        resp = orientacion_schema.dump(orientacion)
        return resp


class CARPOListaRecursos(Resource):
    def get(self):
        CARPOS = Carpo.get_all()
        resultado = carpo_schema.dump(CARPOS, many=True)
        return resultado

    def post(self):
        data = request.get_json()
        carpo_dict = carpo_schema.load(data)
        carpo = Carpo(CarreraID=carpo_dict['CarreraID'],
                      PlanDeEstudioID=carpo_dict['PlanDeEstudioID'], OrientacionID=carpo_dict['OrientacionID'])
        carpo.save()
        resp = carpo_schema.dump(carpo)
        return resp, 201


class CARPORecursos(Resource):
    def get(self, carpo_id):
        carpo = Carpo.get_by_id(carpo_id)
        if carpo is None:
            raise ObjectNotFound(
                'No existe esa Carrera con esa orientación y plan solicitados')
        resp = carpo_schema.dump(carpo)
        return resp
    
    def findorientacionNull(self, carreraid):
        pass


class MateriasListaRecursos(Resource):
    def get(self):
        materias = Materia.get_all()
        resultado = materia_schemas.dump(materias, many=True)
        return resultado

    def post(self):
        data = request.get_json()
        materia_dict = materia_schemas.load(data)
        materia = Materia(
            MateriaNombre=materia_dict['MateriaNombre'], CarpoIDMat=materia_dict['CarpoIDMat'])
        materia.save()
        resp = materia_schemas.dump(materia)
        return resp, 201


class MateriasRecursos(Resource):
    def get(self, materia_id):
        materia = Materia.get_by_id(materia_id)
        if materia is None:
            raise ObjectNotFound(
                'La materia solicitada no existe')
        resp = materia_schema.dump(materia)
        return resp


api.add_resource(CarrerasListaRecursos, '/api/v1.0/carreras/',
                 endpoint='carreras_lista_recursos')

api.add_resource(CarrerasRecursos, '/api/v1.0/carreras/<int:carrera_id>',
                 endpoint='carreras_recursos')

api.add_resource(PlanesListaRecursos, '/api/v1.0/planes/',
                 endpoint='planes_lista_recursos')

api.add_resource(PlanesRecursos, '/api/v1.0/planes/<int:plan_id>',
                 endpoint='planes_recursos')

api.add_resource(OrientacionesListaRecursos, '/api/v1.0/orientaciones/',
                 endpoint='orientaciones_lista_recursos')

api.add_resource(OrientacionesRecursos, '/api/v1.0/orientaciones/<int:orientacion_id>',
                 endpoint='orientaciones_recursos')

api.add_resource(CARPOListaRecursos, '/api/v1.0/carpos/',
                 endpoint='carpos_lista_recursos')

api.add_resource(CARPORecursos, '/api/v1.0/carpos/<int:carpo_id>',
                 endpoint='carpos_recursos')

api.add_resource(MateriasListaRecursos, '/api/v1.0/materias/',
                 endpoint='materias_lista_recursos')

api.add_resource(MateriasRecursos, '/api/v1.0/materias/<int:materia_id>',
                 endpoint='materias_recursos')
