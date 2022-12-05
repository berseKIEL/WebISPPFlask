# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import usuarioDatos, Perfil, Carpo, UsuarioPerfil, personalcarpo,Materia,personalcarpomateria, personalmateriadatos
from ....ext import db

# Desarrollo de la vista docente
docente = Blueprint('docente', __name__)

@docente.route('/miscarreras')
@login_required
def mostrar_carreras_usuarioperfil():
    if session['usuarioperfilactivo'] == 0:
        carpoTotales = Carpo.get_carpo_nombres(db)
        return render_template('user/perfiles/docente/añadircarpo.html', carpo=carpoTotales)
    else:
        # Primero se obitene los carpos que estoy inscriptos
        listaCarpo = personalcarpo.cantcarpo(db, session['personalid'])
        carpoNombres = []
        
        for x in listaCarpo:
            carpoNombres.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
            
        print(carpoNombres)
        
        # Segundo se obtiene, los carpos que me falta inscribirme
        listaCarpoRestante = personalcarpo.get_carpoid_not_personalid(db, session['personalid'])
        carpoRestantes = []
        for x in listaCarpoRestante:
            carpoRestantes.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
        print(carpoRestantes)
        
        return render_template('user/perfiles/docente/miscarreras.html', carposUsuario = carpoNombres, carpo = carpoRestantes)


@docente.route('/datossecundaria')
@login_required
def mostrar_datossecundaria_usuarioperfil():
    return render_template('user/perfiles/docente/datossecundaria.html')

@docente.route('/seleccionarmaterias', methods=['POST'])
@login_required
def seleccionar_materias():
    carpoid = request.form.get('Carpo')
    if (carpoid==None):
        flash('No puedes inscribirte sin seleccionar una carrera')  
        return redirect(url_for('docente.mostrar_carreras_usuarioperfil'))  
    else:
        materias = Materia.get_materia_by_carpoidmat(db,carpoid)
        print(type(materias))
        
        return render_template('user/perfiles/docente/seleccionmateria.html',carpoid = carpoid, materias = materias)

@docente.route('/Eliminarcarrera', methods = ['POST'])
@login_required
def eliminar_carrera():
    carpoid = request.form.get('carpoid')
    personalcarpo.eliminar_personalcarpo(db,session['personalid'], carpoid)


    if len(personalcarpo.cantcarpo(db,session['personalid'])) == 0:
        UsuarioPerfil.deactivate_user_perfil(db, current_user.id, session['perfilid'])
        session['usuarioperfilactivo'] = 0

    return redirect(url_for('docente.mostrar_carreras_usuarioperfil'))

@docente.route('/Vermaterias', methods = ['POST'])
@login_required
def Ver_Materias():
    carpoid = request.form.get('carpoid')
    personalcarpoid = personalcarpo.get_personalcarpoid(db,session['personalid'],carpoid)[0]
    personalcarpomaterias = personalcarpomateria.select_personalcarpomateria_by_personalcarpoid(db,personalcarpoid)
    materias = []
    for i in personalcarpomaterias:
        materias.append(Materia.get_Materia_id(db, i[2]))
    print(materias)

    return render_template('user/perfiles/docente/vermaterias.html', materias = materias)


@docente.route('/activarperfil', methods=['POST'])
@login_required
def activar_usuarioperfil():
    carpoid = request.form.get('carpoid')
    materiaid = request.form.get('materia')

    CargaHoraria = request.form.get('CargaHoraria')
    SituacionRevista = request.form.get('SituacionRevista')
    FechaInCargo = request.form.get('FechaInCargo')
    TurnoCargo = request.form.get('TurnoCargo')
    NumControl = request.form.get('NumControl')
    TituloProfesional = request.form.get('TituloProfesional')
    observaciones = request.form.get('observaciones')

    if ((((((CargaHoraria == '') or SituacionRevista == '') or FechaInCargo == '') or TurnoCargo == '') or NumControl == '') or TituloProfesional == ''):

        flash('faltan completar datos')
        materias = Materia.get_materia_by_carpoidmat(db,carpoid)
        return render_template('user/perfiles/docente/seleccionmateria.html',carpoid = carpoid, materias = materias)

    else:
        personalcarpoid = personalcarpo.cargar_personalcarpo(db,session['personalid'], carpoid)[1]
        personalcarpomateriaid = personalcarpomateria.cargar_personalcarpomateria(db,personalcarpoid,materiaid)

        personalmateriadatos.insert_into_personalmateriadatos(db,personalcarpomateriaid,CargaHoraria,SituacionRevista,FechaInCargo,TurnoCargo,NumControl,TituloProfesional,observaciones)

        if 'usuarioperfilactivo' in session:
            if session['usuarioperfilactivo'] == 0:
                UsuarioPerfil.activate_user_perfil(db, current_user.id, session['perfilid'])
                session['usuarioperfilactivo'] = 1
        
        return redirect(url_for('docente.mostrar_carreras_usuarioperfil'))

@docente.route('/agregarcarrera', methods = ['POST'])
@login_required
def agregar_carrera():
    
    carpoid = request.form.get('Carpo')
    
    if (carpoid==None):
        flash('No puedes inscribirte sin seleccionar una carrera')    
    else:
        alumnocarpo.insert_alumnocarpo(db, session['alumnoid'], carpoid)
        
    return redirect(url_for('docente.mostrar_carreras_usuarioperfil'))