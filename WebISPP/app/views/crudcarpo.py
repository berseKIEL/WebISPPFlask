from flask import Blueprint, render_template, flash, request

import json

from ..entidades.carrera import Carrera
from ..common.request import get_request_json

crudcarpo = Blueprint("crudcarpo", __name__)

# @crudcarpo.route('/carreras', methods=['GET','POST'])
# def mostrarCarreras():
#     # if request.method == 'POST':
#     #     action=request.form['accion']
#     #     if action=="dbclickcarrera":
#     #         idcarrera=request.form['idcarrera']
#     #         idorientacion=request.form['idorientacion']
#     #         orientaciones=Orientacion.listarOrientacionPorCarrera(mysql,idcarrera)

#     #         if idorientacion != "-1":
#     #             orientaciones=None

#     #         if orientaciones==None:
#     #             #retorno planes
#     #             if idorientacion != "-1":
#     #                 plan=Planes.listarPlanesPorCarreraYOrientacion(mysql,idcarrera,idorientacion)
#     #             else:
#     #                 plan=Planes.listarPlanesPorCarrera(mysql,idcarrera)

#     #             nombre="Planes"
#     #             return render_template("planes.html",planes=plan,nombre=nombre, idcarrera=idcarrera, idorientacion=idorientacion)
#     #         else:
#     #             #retorno orientaciones
#     #             nombre="Orientaciones"
#     #             return render_template("orientaciones.html",ori=orientaciones,idcarr=idcarrera,nombre=nombre)
        
#     #     else:
#     #         if action=="mostrarmaterias":
#     #             idplan=request.form['idplan']
#     #             idcarrera = request.form['idcarrera']
#     #             idorientacion = request.form['idorientacion']
                
#     #             idcarpo = Carpo.buscarcarpo(mysql,idcarrera,idorientacion,idplan)
                
#     #             nombrecarpo = Carpo.nombreCarpo(mysql,idcarpo)
#     #             materias=Materia.listarMaterias(mysql,idcarpo)
#     #             año=Materia.cantidadDeAños(mysql,idcarpo)
#     #             lista_años = [1,2,3,4,5,6]
#     #             años=['Primer año','Segundo año','Tercer año','Cuarto año','Quinto año']
#     #             return render_template("materias.html",materias=materias, listaAños=años, cantidadAños=año,idcarpo=idcarpo, listaañonumerica=lista_años, nombre = nombrecarpo)
        
#     # lista = Carreras.listarCarreras(mysql)
#     # nombre="Carreras"
#     return render_template("carreras.html",lista=lista,nombre=nombre)


@crudcarpo.route('/get_carreras',methods=['GET','POST',])
def mostrarCarrerasPrueba():
    
    nombres = ['Carreras','Orientaciones','Planes']
    listacar=[]
    
    if request.method == 'GET':
        listacar = Carrera.buscarAPI()
        print(listacar)
    
    if request.method == 'POST':
        output=request.get_json()
        print(output)
        return output
        
    return render_template("crudcarpo.html", lista = listacar,nombres=nombres)

