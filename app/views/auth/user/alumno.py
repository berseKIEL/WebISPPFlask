# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import usuarioDatos, Perfil, Carpo, alumnocarpo, UsuarioPerfil, alumnodomproc, alumnosecundaria,Materia,alumnocarpomateria
from ....ext import db

# Desarrollo de la vista Alumno
alumno = Blueprint('alumno', __name__)

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

@alumno.route('/agregarMateria', methods = ['POST'])
@login_required
def agregar_materia():
    carpoid = request.form.get('carpoid')
    materiaid = request.form.get('materia')
    alumnocarpoid = request.form.get('alumnocarpoid')

    print(alumnocarpoid, ' alumnocarpoid')
    alumnocarpomateria.insert_alumnocarpomateria(db,materiaid, alumnocarpoid)

    return redirect(url_for('alumno.mis_materias', carpoid=carpoid))

@alumno.route('/borrarMateria', methods = ['POST'])
@login_required
def borrar_materia():
    carpoid = request.form.get('carpoid')
    materiaid = request.form.get('materiaid')
    alumnocarpoid = request.form.get('alumnocarpoid')

    print(alumnocarpoid, ' alumnocarpoid ', materiaid, ' materiaid')
    alumnocarpomateria.delete_alumnocarpomateria(db,materiaid, alumnocarpoid)

    return redirect(url_for('alumno.mis_materias', carpoid=carpoid))


@alumno.route('/Materias', methods = ['POST','GET'])
@login_required
def mis_materias():
    if request.method == 'POST':
        carpoid = request.form.get('carpoid')
    else:
        carpoid = request.args.get('carpoid')
        #Obtiene materias para inscribir
    if (carpoid==None):
        flash('No puedes inscribirte sin seleccionar una carrera')  
        return redirect(url_for('alumno.mostrar_carreras_usuarioperfil'))  
    else:
        print(carpoid,'  sadasd ',session['alumnoid'])
        alumnocarpoid = alumnocarpo.get_alumnocarpoid_by_alumnoidcarpoid(db,carpoid,session['alumnoid'])

        if alumnocarpoid == None:
            materias = Materia.get_materia_by_carpoidmat(db,carpoid)
        else:
            materias = Materia.get_materia_by_alumno_filtrer(db,alumnocarpoid[0],carpoid)

    #Obtiene materias inscriptas
    materiasinscriptasid = alumnocarpomateria.get_materiaid_by_alumnocarpoid(db,alumnocarpoid)
    if materiasinscriptasid == None:
        materiasinscriptas = materiasinscriptasid
    else:
        materiasinscriptas = Materia.get_materia_by_alumno_filtrerIn(db,alumnocarpoid[0],carpoid)
    return render_template('user/perfiles/alumno/seleccionarmateria.html', materias = materias, alumnocarpoid = alumnocarpoid[0][0], carpoid = carpoid, materiasinscriptas = materiasinscriptas)
    


@alumno.route('/datossecundaria', methods=['GET','POST'])
@login_required
def mostrar_datossecundaria_usuarioperfil():
    if request.method == 'GET':
        alumnoid = session['alumnoid']
        datosecundaria = alumnosecundaria.get_alumno_alumnosecundaria_id(db, alumnoid)
        
    if request.method == 'POST':
        institucion = request.form.get('institucion')
        titulosec = request.form.get('titulosec')
        modalidad = request.form.get('modalidad')
        añoEgreso = request.form.get('añoEgreso')

        error = None
        
        if not institucion and not institucion.strip():
            error = 'Falta completar la institucion'
        
        if not titulosec and not titulosec.strip():
            error = 'Falta completar el Titulo'
        
        if not modalidad and not modalidad.strip():
            error = 'Falta completar la modalidad'
        
        if not añoEgreso and not añoEgreso.strip():
            error = 'Falta completar el año de Egreso'
        
        if not error:
            alumnosecundaria.update_alumnosecundaria(db,institucion,titulosec,modalidad,añoEgreso,session['alumnoid'])
            flash('Se modifico los datos correctamente',category='success')
            return redirect(url_for('alumno.mostrar_datossecundaria_usuarioperfil'))
        
        else:
            flash(error)
            return redirect(url_for('alumno.mostrar_datossecundaria_usuarioperfil'))
            
    return render_template('user/perfiles/alumno/datossecundaria.html', datosecundaria = datosecundaria)


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

@alumno.route('/edit/datosdomicilioproc', methods=['POST'])
@login_required
def editar_datosdomicilioproc_alumno():
    provincia = request.form.get('provincia')
    departamento = request.form.get('departamento')
    localidad = request.form.get('localidad')
    ciudad = request.form.get('ciudad')
    barrio = request.form.get('barrio')
    calle = request.form.get('calle')
    altura = request.form.get('altura')
    piso = request.form.get('piso')
    numdep = request.form.get('numdep')
    manzana = request.form.get('manzana')
    cp = request.form.get('cp')

    error = None

    if not provincia and not provincia.strip():
        error = 'Falta completar la provincia'

    if not departamento and not departamento.strip():
        error = 'Falta completar la departamento'

    if not localidad and not localidad.strip():
        error = 'Falta completar el localidad'

    if not ciudad and not ciudad.strip():
        error = 'Falta completar el ciudad'

    if not barrio and not barrio.strip():
        error = 'Falta completar el barrio'

    if not calle and not calle.strip():
        error = 'Falta completar el calle'

    if not altura and not altura.strip():
        error = 'Falta completar la altura'

    if not piso and not piso.strip():
        error = 'Falta completar el Piso'

    if not numdep and not numdep.strip():
        error = 'Falta completar el Numero de departamento'

    if not manzana and not manzana.strip():
        error = 'Falta completar la manzana'

    if not cp and not cp.strip():
        error = 'Falta completar el Codigo Postal'

    if not (error):
        alumnodomproc.update_usuariodomproc(db,provincia, departamento, localidad,ciudad, barrio, calle, altura, piso, numdep, manzana, cp, current_user.id)

    else:
        flash(error)
        return redirect(url_for('usuario.mostrar_Datospersonales_usuarioperfil'))
