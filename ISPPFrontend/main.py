from queue import Empty
from flask import Flask, redirect, url_for,flash,render_template,request
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask.json import jsonify
from config import config
from models.entidades.carreras import Carreras
from models.entidades.planes import Planes
from models.entidades.materia import Materia
from models.entidades.orientacion import Orientacion
from models.entidades.carpo import Carpo

from models.entidades.usuario import User
from models.modelUser import modeluser

app= Flask(__name__)
csrf = CSRFProtect()
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template("inicio.html")


@app.route('/carreras', methods=['GET','POST'])
def mostrarCarreras():
    if request.method == 'POST':
        action=request.form['accion']
        if action=="dbclickcarrera":
            idcarrera=request.form['idcarrera']
            idorientacion=request.form['idorientacion']
            orientaciones=Orientacion.listarOrientacionPorCarrera(mysql,idcarrera)

            if idorientacion != "-1":
                orientaciones=None

            if orientaciones==None:
                #retorno planes
                if idorientacion != "-1":
                    plan=Planes.listarPlanesPorCarreraYOrientacion(mysql,idcarrera,idorientacion)
                else:
                    plan=Planes.listarPlanesPorCarrera(mysql,idcarrera)

                nombre="Planes"
                return render_template("planes.html",planes=plan,nombre=nombre, idcarrera=idcarrera, idorientacion=idorientacion)
            else:
                #retorno orientaciones
                nombre="Orientaciones"
                return render_template("orientaciones.html",ori=orientaciones,idcarr=idcarrera,nombre=nombre)
        
        else:
            if action=="mostrarmaterias":
                idplan=request.form['idplan']
                idcarrera = request.form['idcarrera']
                idorientacion = request.form['idorientacion']
                
                idcarpo = Carpo.buscarcarpo(mysql,idcarrera,idorientacion,idplan)
                
                nombrecarpo = Carpo.nombreCarpo(mysql,idcarpo)
                materias=Materia.listarMaterias(mysql,idcarpo)
                año=Materia.cantidadDeAños(mysql,idcarpo)
                lista_años = [1,2,3,4,5,6]
                años=['Primer año','Segundo año','Tercer año','Cuarto año','Quinto año']
                return render_template("materias.html",materias=materias, listaAños=años, cantidadAños=año,idcarpo=idcarpo, listaañonumerica=lista_años, nombre = nombrecarpo)
        
    lista = Carreras.listarCarreras(mysql)
    nombre="Carreras"
    return render_template("carreras.html",lista=lista,nombre=nombre)

@app.route('/cargarMaterias', methods=['GET','POST'])
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


@app.route('/cargarCarreras', methods=['GET','POST'])
def cargarCarrera():
    listap=Planes.listarPlanes(mysql)
    listao=Orientacion.listarOrientaciones(mysql)
    
    if request.method == 'POST':
        carrera=request.form['nombrecarrera']
        orientacion=request.form['orientaciones']
        plan=request.form['planes']
        
        if Carreras.obtenerID(mysql,carrera)=='vacio':
            Carreras.AgregarCarrera(mysql,carrera)
            carrera=Carreras.obtenerID(mysql,carrera)
            
            if plan=='otro':
                #Agrego plan
                plan=request.form['otro_plan']
                if Planes.obtenerID(mysql,plan) =='vacio':
                    Planes.AgregarPlan(mysql,plan)
            plan=Planes.obtenerID(mysql,plan)

            if orientacion!='Null':
                if orientacion=='otra':
                    #Agrego 
                    orientacion=request.form['otra_orientacion']
                    if Orientacion.obtenerID(mysql,orientacion)=='vacio':
                        Orientacion.AgregarOrientacion(mysql,orientacion)
                orientacion=Orientacion.obtenerID(mysql,orientacion)
            
            #carpo
            Carpo.AgregarCarpo(mysql,carrera,orientacion,plan)
            flash('Carrera Agregada!')
                   
        else:
            flash('Carrera Existente')
        
    return render_template("cargarCarreras.html",listap=listap,lista=listao)




def status_401(error):
    flash('Debes iniciar session para acceder')
    return redirect(url_for('index'))
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['desarrollo'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(port=2432)