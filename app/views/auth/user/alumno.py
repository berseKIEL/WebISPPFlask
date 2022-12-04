# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import usuarioDatos, Perfil, Carpo, alumnocarpo, UsuarioPerfil
from ....ext import db

# Desarrollo de la vista Alumno
alumno = Blueprint('alumno', __name__)


@alumno.before_request
def before_request():
    try:
        print(session['usuarioperfilactivo'])
    except:
        print('caca')        


@alumno.route('/miscarreras')
@login_required
def mostrar_carreras_usuarioperfil():
    carpoTotales = Carpo.get_carpo_nombres(db)
    if session['usuarioperfilactivo'] == 0:
        return render_template('user/perfiles/alumno/añadircarpo.html', carpo=carpoTotales)
    else:
        # Primero se obitene los carpos que estoy inscriptos
        listaCarpo = alumnocarpo.get_carpoid_by_alumnoid(db, session['alumnoid'])
        carpoNombres = []
        
        for x in listaCarpo:
            carpoNombres.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
            
        print(carpoNombres)
        
        # Segundo se obtiene, los carpos que me falta inscribirme
        listaCarpoRestante = alumnocarpo.get_carpoid_not_alumnoid(db, session['alumnoid'])
        carpoRestantes = []
        for x in listaCarpoRestante:
            carpoRestantes.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
        
        return render_template('user/perfiles/alumno/miscarreras.html', carposUsuario = carpoNombres, carpo = carpoRestantes)


@alumno.route('/datossecundaria')
@login_required
def mostrar_datossecundaria_usuarioperfil():
    return render_template('user/perfiles/alumno/datossecundaria.html')


@alumno.route('/activarperfil', methods=['POST'])
@login_required
def activar_usuarioperfil():
    carpoid = request.form.get('Carpo')

    if alumnocarpo.insert_alumnocarpo(db, session['alumnoid'], carpoid):
        UsuarioPerfil.activate_user_perfil(db, current_user.id, session['perfilid'])
        session['usuarioperfilactivo'] = 1
        
    return redirect(url_for('alumno.mostrar_carreras_usuarioperfil'))

@alumno.route('/agregarcarrera', methods = ['POST'])
@login_required
def agregar_carrera():
    
    carpoid = request.form.get('Carpo')
    
    if (carpoid==None):
        flash('No puedes inscribirte sin seleccionar una carrera')    
    else:
        alumnocarpo.insert_alumnocarpo(db, session['alumnoid'], carpoid)
        
    return redirect(url_for('alumno.mostrar_carreras_usuarioperfil'))