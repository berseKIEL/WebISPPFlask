from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from flask_login import current_user

from ..models.models import Carpo, Plan, Carrera, Materia

from ..ext import db


home = Blueprint("home", __name__)

@home.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('auth.verificar_roles'))
    return render_template("home.html")


@home.route('/carreras', methods=['GET','POST'])
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
                    return render_template("oferta-academica.html",lista=plan,nombre=nombre, listaValores = listaValores )
                else:
                    #retorno orientaciones
                    nombre = Plan.get_nombre_ori_plan(db, listaValores[0], -1)
                    nombre = nombre + "Orientaciones"
                    return render_template("oferta-academica.html",lista=orientaciones,nombre=nombre,listaValores=listaValores)
        
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
    
    return render_template("oferta-academica.html",lista=listaCarreras,nombre=nombre,listaValores=listaValores)