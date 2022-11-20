from flask import Blueprint, request, render_template, jsonify, flash, session

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
    session['listadeValores'] = [-1,-1,-1]
   
    listaValores = session['listadeValores']
        
    if request.method == 'POST':
        action=request.form['accion']
        if action=="dbclickcarrera":
            listaValores[0]=int(request.form['carreraid'])
            listaValores[1]=int(request.form['orientacionid'])
            listaValores[2]=int(request.form['planid'])

            if listaValores[2]==-1:
                orientaciones = Carpo.get_result_ori(db, listaValores[0])

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
                session.pop('listadeValores')
                return render_template("materias.html",materias=materias, listaAños=años, cantidadAños=año,idcarpo=idcarpo, listaañonumerica=lista_años, nombre = nombrecarpo)
            
    listaCarreras = Carrera.get_Carrera_all(db)
    
    nombre="Carreras"
    
    return render_template("carreras.html",lista=listaCarreras,nombre=nombre,listaValores=listaValores)

@crudcarpo.route('/cargarMaterias', methods=['POST'])
def cargarMaterias():
    if request.method=='POST':
        new_data = request.get_json()
        
        materianombre = new_data['MateriaNombre']
        materiaaño = new_data['MateriaAño']
        materiatipo = new_data['MateriaTipo']
        carpoidmat = new_data['CarpoID']
        
        materiaid = Materia.add_Materia(db, materianombre, materiaaño, materiatipo, carpoidmat)
        
        MateriaCargada = {'ID de la Materia': materiaid,'Nombre de la Materia':materianombre,'Año de la Materia':materiaaño,'Tipo de Materia':materiatipo,'CARPO':carpoidmat}
        
        flash('Materia Agregada!')
        
    return jsonify({'Mensaje':'Se ha cargado la materia se forma Exitosa!', 'Materia Cargada':MateriaCargada})


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

@crudcarpo.route('/editar', methods=['GET','PUT'])
def editarCarpo():
    if request.method == 'GET':
        carpoid = request.args.get('id')
        nombrecar = request.args.get('carrera')
        get_carpo = Carpo.get_ori_plan_carpo(db, carpoid)
        
        print(get_carpo)
        Planes = []
        for plan in get_carpo[0]:
            for planes in plan:
                Planes.append(planes)
                
        Orientaciones = []
        for orien in get_carpo[1]:
            for orienta in orien:
                Orientaciones.append(orienta)
                
    if request.method == 'PUT':
        pass
    
    return render_template('editarborrarcarrera.html',Planes=Planes,Orientaciones=Orientaciones,nombrecar=nombrecar)

@crudcarpo.route('/eliminar',methods=['GET'])
def eliminarSeleccionado():
    idseleccionada = request.args.get('idseleccionada')
    cSelec = request.args.get('c')
    oSelec = request.args.get('o')
    pSelec = request.args.get('p')
    lista = [cSelec, oSelec, pSelec]
    
    if lista[0] == "-1":
        # borrar todos los carpos de la carrera seleccionada
        print(Carrera.get_Carrera_id(db, idseleccionada))
    elif lista[0] != "-1":
        if lista[1] == "0":
             # borrar carpo del plan de la carrera seleccionado
            print(Carrera.get_Carrera_id(db, cSelec))
            print(Plan.get_Plan_id(db, idseleccionada))
        elif lista[1] == "-1":
            # borrar orientacion de la carrera seleccionada
            print(Carrera.get_Carrera_id(db, cSelec))
            print(Orientacion.get_Orientacion_id(db, idseleccionada))
        else:
            # borrar plan dentro de una orientacion de una carrera seleccionada
            print(Carrera.get_Carrera_id(db, cSelec))
            print(Orientacion.get_Orientacion_id(db, oSelec))
            print(Plan.get_Plan_id(db, idseleccionada))
        
    print(idseleccionada)
    print(lista)
    return jsonify({'Eliminada':'OK'})