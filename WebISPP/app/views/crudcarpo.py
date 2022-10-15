from flask import Blueprint, request, render_template, jsonify, flash

from ..models.carrera import Carrera
from ..models.orientacion import Orientacion
from ..models.plan import Plan
from ..models.carpo import Carpo
from ..models.materia import Materia

from ..common.convertoInt import convertInt

from ..ext import db

crudcarpo = Blueprint("crudcarpo", __name__)

@crudcarpo.route('/carreras', methods=['GET','POST'])
def mostrarCarreras():    
    listaValores = [-1, -1, -1]
        
    if request.method == 'POST':
        action=request.form['accion']
        if action=="dbclickcarrera":
            listaValores[0]=int(request.form['carreraid'])
            listaValores[1]=int(request.form['orientacionid'])
            listaValores[2]=int(request.form['planid'])

            if listaValores[2]==-1:
                orientaciones = Carpo.get_result_ori(db, listaValores[0])
                print(listaValores)
                print(orientaciones)

                if listaValores[1] != -1:
                    orientaciones=None

                if orientaciones==None:
                    #retorno planes
                    if listaValores[1] != -1:
                        plan=Plan.get_plan_via_oricar(db,listaValores[0], listaValores[1])
                    else:
                        listaValores[1]=0
                        plan=Plan.get_plan_via_car(db,listaValores[0])
                    print(plan)
                    nombre = Plan.get_nombre_ori_plan(db, listaValores[0], listaValores[1])
                    nombre= nombre+"Planes"
                    return render_template("carreras.html",lista=plan,nombre=nombre, listaValores = listaValores )
                else:
                    #retorno orientaciones
                    nombre = Plan.get_nombre_ori_plan(db, listaValores[0], -1)
                    nombre = nombre + "Orientaciones"
                    return render_template("carreras.html",lista=orientaciones,nombre=nombre,listaValores=listaValores)
        
            else:
                print(listaValores)                
                idcarpo = Carpo.search_carpo(db,listaValores[0],listaValores[1],listaValores[2])
                
                nombrecarpo = Carpo.name_carpo(db,idcarpo)
                materias=Materia.get_Materia_all(db,idcarpo)
                año=Materia.cantidadDeAños(db,idcarpo)
                lista_años = [1,2,3,4,5,6]
                años=['Primer año','Segundo año','Tercer año','Cuarto año','Quinto año']
                return render_template("materias.html",materias=materias, listaAños=años, cantidadAños=año,idcarpo=idcarpo, listaañonumerica=lista_años, nombre = nombrecarpo)
            
    listaCarreras = Carrera.get_Carrera_all(db)
    
    nombre="Carreras"
    
    return render_template("carreras.html",lista=listaCarreras,nombre=nombre,listaValores=listaValores)

@crudcarpo.route('/cargarMaterias', methods=['GET','POST'])
def cargarMaterias():
    if request.method=='POST':
        nombreMateria=request.form['nombreMateria']
        añoMateria=request.form['añoMateria']
        tipoMateria=request.form['tipomateria']
        idcarpoM=request.form['idcarpo']

        #guardar materia
        Materia.agregarMateria(mysql,nombreMateria, añoMateria, tipoMateria,idcarpoM)

        nombrecarpo = Carpo.nombreCarpo(mysql,idcarpoM)
        materias=Materia.listarMaterias(mysql,idcarpoM)
        año=Materia.cantidadDeAños(mysql,idcarpoM)
        lista_años = [1,2,3,4,5,6]
        años=['Primer año','Segundo año','Tercer año','Cuarto año','Quinto año']
    
    return render_template("materias.html",materias=materias, listaAños=años, cantidadAños=año,idcarpo=idcarpoM, listaañonumerica=lista_años,nombre = nombrecarpo)


@crudcarpo.route('/cargarCarreras', methods=['POST'])
def cargarCarrera():
    if request.method == 'POST':
        new_data = request.get_json()
        carrera = new_data['carrera']
        orientacion = new_data['orientacion']
        plan = new_data['plan']
        print(new_data)

    
        carreraid = Carrera.add_Carrera(db, carrera)
        
        #Crear Plan
        planid = convertInt(plan)
        
        if planid == False:
           planid = Plan.add_Plan(db, plan) 
           
        #Crear Orientacion
        orientacionid = convertInt(orientacion)
        
        if orientacionid == False:
            if orientacion != 'null':
                orientacionid = Orientacion.add_Orientacion(db, orientacion)

        carpoid = Carpo.add_Carpo(db, carreraid, planid, orientacionid)
        
        CarreraCargada = {'Carpo':carpoid,'Carrera':carreraid,'Plan':planid,'Orientacion':orientacionid}
    
        flash('Carrera Agregada!')
        
    return jsonify({'Mensaje':'La carrera se cargo exitosamente!','Carrera':CarreraCargada})

@crudcarpo.route('/get_ori_plan', methods=['GET','POST'])
def get_ori_plan():
    planes = Plan.get_Plan_all(db)
    orien = Orientacion.get_Orientacion_all(db)

    listaPlanes = []
    listaOri = []
    
    for fila in planes:
        plan = {'PlanID':fila[0],'PlanNombre':fila[1]}
        listaPlanes.append(plan)
    
    for fila in orien:
        ori = {'OrientacionID':fila[0],'OrientacionNombre':fila[1]}
        listaOri.append(ori)
    return jsonify({'Planes':listaPlanes,'Orientaciones':listaOri,'Mensaje':'Sucess'})