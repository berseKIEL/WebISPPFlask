# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import usuarioDatos, Perfil, Carpo, UsuarioPerfil, personalcarpo,Materia,personalcarpomateria, personalmateriadatos,alumnocarpo,alumno
from ....ext import db

# Desarrollo de la vista docente
docente = Blueprint('docente', __name__)

@docente.route('/miscarreras')
@login_required
def mostrar_carreras_usuarioperfil():
    carpoTotales = Carpo.get_carpo_nombres(db)
    print(len(personalcarpo.cantcarpo(db,session['personalid'])), ' condicion')
    if session['usuarioperfilactivo'] == 0:
        
        return render_template('user/perfiles/docente/añadircarpo.html', carpo=carpoTotales)
    else:
        # Primero se obitene los carpos que estoy inscriptos
        listaCarpo = personalcarpo.cantcarpo(db, session['personalid'])
        carpoNombres = []
        
        for x in listaCarpo:
            carpoNombres.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
        
        return render_template('user/perfiles/docente/miscarreras.html', carposUsuario = carpoNombres, carpo = carpoTotales)


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
        #falta filtrar materias inscriptas
        personalcarpoid = personalcarpo.get_personalcarpoid(db,session['personalid'], carpoid)

        if personalcarpoid == None:
            materias = Materia.get_materia_by_carpoidmat(db,carpoid)
        else:
            materias = Materia.get_materia_by_carpoidmat_filtrer(db,personalcarpoid[0],carpoid)

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

@docente.route('/Materias', methods = ['POST'])
@login_required
def Ver_Materias():
    carpoid = request.form.get('carpoid')
    personalcarpoid = personalcarpo.get_personalcarpoid(db,session['personalid'],carpoid)[0]
    personalcarpomaterias = personalcarpomateria.select_personalcarpomateria_by_personalcarpoid(db,personalcarpoid)
    materias = []
    for i in personalcarpomaterias:
        materias.append(Materia.get_Materia_id(db, i[2]))

    return render_template('user/perfiles/docente/vermaterias.html', materias = materias, personalcarpoid = personalcarpoid,carpoid = carpoid)


@docente.route('/EliminarMateria', methods = ['POST'])
@login_required
def eliminarmateria_personalcarpomateria():
    carpoid = request.form.get('carpoid')    
    personalcarpoid = request.form.get('personalcarpoid')
    materiaid = request.form.get('materiaid')
    if personalcarpomateria.eliminar_personalcarpomateria(db,personalcarpoid,materiaid):
        flash('Se desinscribio de una materia')
        personalcarpomateriaid = personalcarpomateria.select_personalcarpomateria(db,personalcarpoid)
        if personalcarpomateriaid == None:
            print('if eliminar')
            print(session['personalid'],carpoid, ' personalid, carpoid')
            personalcarpo.eliminar_personalcarpo(db,session['personalid'],carpoid)

            print(len(personalcarpo.cantcarpo(db,session['personalid'])), 'condicion 2do if')

            if len(personalcarpo.cantcarpo(db,session['personalid'])) == 0:
                print('if eliminar 2')
                UsuarioPerfil.deactivate_user_perfil(db, current_user.id, session['perfilid'])
                session['usuarioperfilactivo'] = 0

            return redirect(url_for('docente.mostrar_carreras_usuarioperfil'))

    personalcarpomaterias = personalcarpomateria.select_personalcarpomateria_by_personalcarpoid(db,personalcarpoid)
    materias = []
    for i in personalcarpomaterias:
        materias.append(Materia.get_Materia_id(db, i[2]))

    return render_template('user/perfiles/docente/vermaterias.html', materias = materias, personalcarpoid = personalcarpoid, carpoid = carpoid)


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
        personalcarpoid = personalcarpo.get_personalcarpoid(db,session['personalid'], carpoid)

        if personalcarpoid == None:
            personalcarpoid = personalcarpo.cargar_personalcarpo(db,session['personalid'], carpoid)[1]
        else:
            personalcarpoid = personalcarpoid[0]
        

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

@docente.route('/Materias/Datos', methods = ['POST'])
@login_required
def Ver_Datos():
    #datos materias
    materiaid = request.form.get('materiaid')
    carpoid = request.form.get('carpoid')
    personalcarpoid = request.form.get('personalcarpoid')
    personalcarpomateriaid = personalcarpomateria.get_personalcarpomateriaid(db,personalcarpoid,materiaid)[0]
    datosmateria = personalmateriadatos.select_personalmateriadatos(db,personalcarpomateriaid)[0]

    materia = Materia.get_Materia_id(db,materiaid)
    alumnosid = alumnocarpo.get_alumnoid(db,materia[0])



    usuariosperfilesid =[]
    for i in alumnosid:
        usuariosperfilesid.append([alumno.get_usuarioperfil_from_alumno(db,i[0]),i[0]])
    usuariosid = []
    for i in usuariosperfilesid:
        usuariousuarioperfil=UsuarioPerfil.get_usuarioid_from_usuarioperfil(db,i[0])
        usuariousuarioperfil.append(i[1])
        usuariosid.append(usuariousuarioperfil)

    
    nombreapellido = []
    user = []
    for i in usuariosid:
        
        user = list(usuarioDatos.get_Nombre_Apellido_from_usuariodatos(db,i[0]))

        user.append(i[2]) 

        user.append(i[0])

        nombreapellido.append(user)
        
    return render_template('user/perfiles/docente/verdatos.html',datosmateria = datosmateria, materia = materia, nombreapellido = nombreapellido)
