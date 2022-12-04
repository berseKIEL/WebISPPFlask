# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ...models.models import Perfil, UsuarioPerfil, alumno, personal, usuarioDatos, usuarioDomicilio, alumnodomproc, Usuario
from ...ext import db

# Desarrollo de la vista usuario
usuario = Blueprint('usuario', __name__)


@usuario.route('/')
@login_required
def index():
    # Obtener el perfil que es
    perfilid = 0
    session['usuarioperfilid'] = UsuarioPerfil.get_usuarioperfilid(
        db, current_user.id, session['perfilid'])

    if session['perfilid'] != 7:
        session['personalid'] = personal.get_personalid(
            db, session['usuarioperfilid'])
            
    else:
        session['alumnoid'] = alumno.get_alumnoid_by_usuarioperfilid(
            db, session['usuarioperfilid'])

    if session['perfilid']:
        perfilid = session['perfilid']

    perfil = Perfil.get_perfil_via_id(db, perfilid)[0][1]
    consulta = usuarioDatos.get_usuario_datos_id(db, current_user.id)
    return render_template('user/home.html', perfil=perfil, consulta=consulta)

# Se utiliza para obtener el nombre del perfil que selecciono actualmente


@usuario.route('/obtenernombredelperfil')
@login_required
def obtener_nombre_perfil():
    perfilid = 0
    if 'perfilid' in session:
        perfilid = session['perfilid']
    perfiles = Perfil.get_perfil_via_id(db, perfilid)[0][1]
    return jsonify({'Respuesta': perfiles})


@usuario.route('/obtenercountperfil')
@login_required
def obtener_count_perfiles():
    perfiles = UsuarioPerfil.get_count_usuarioperfil(db, current_user.id)[0]
    return jsonify({'Respuesta': perfiles})


@usuario.route('/datospersonales')
@login_required
def mostrar_Datospersonales_usuarioperfil():
    # Obtener DatosPersonales
    datosPersonales = usuarioDatos.get_usuario_datos_id(db, current_user.id)

    datosDomicilio = usuarioDomicilio.get_usuario_domicilio_id(
        db, current_user.id)

    perfilid = session['perfilid']

    alumnoid = session['alumnoid']

    if perfilid == 7:
        datosDomicilioProc = alumnodomproc.get_usuario_domproc_id(db, alumnoid)
        return render_template('user/perfiles/Datospersonales.html', datosPersonales=datosPersonales, datosDomicilio=datosDomicilio, datosDomicilioProc=datosDomicilioProc)

    return render_template('user/perfiles/Datospersonales.html', datosPersonales=datosPersonales, datosDomicilio=datosDomicilio)


@usuario.route('/edit/datospersonales', methods=['POST'])
@login_required
def editar_datospersonales_usuario():
    cuil = request.form.get('cuil')
    nac = request.form.get('nacionalidad')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    fecnac = request.form.get('fechanac')
    sexodni = request.form.get('sexodni')

    error = None

    if not cuil and not cuil.strip():
        error = 'Falta completar el CUIL'

    if not nac and not nac.strip():
        error = 'Falta completar la Nacionalidad'

    if not nombre and not nombre.strip():
        error = 'Falta completar el Nombre'

    if not apellido and not apellido.strip():
        error = 'Falta completar el Apellido'

    if not email and not email.strip():
        error = 'Falta completar el email'

    if not telefono and not telefono.strip():
        error = 'Falta completar el telefono'

    if not fecnac and not fecnac.strip():
        error = 'Falta completar la Fecha de Nacimiento'

    if not sexodni and not sexodni.strip():
        error = 'Falta completar el Genero del DNI'

    if not (error):
        usuarioDatos.update_usuariodatos(db, current_user.id, nombre, apellido, cuil, fecnac, sexodni, nac, telefono)

        correo = Usuario.get_usuario_correo(db, email)[0]
        
        if not correo:
            Usuario.update_email(db, email, current_user.id)
            flash('¡Datos actualizado Correctamente!',category='success')
            return redirect(url_for('usuario.mostrar_Datospersonales_usuarioperfil'))
        if correo == email:
            flash('¡Datos actualizado Correctamente!',category='success')
            return redirect(url_for('usuario.mostrar_Datospersonales_usuarioperfil'))
        else:
            flash('Se actualizo los datos a Excepción del correo: - Ya existe -')
            return redirect(url_for('usuario.mostrar_Datospersonales_usuarioperfil'))

    else:
        flash(error)
        return redirect(url_for('usuario.mostrar_Datospersonales_usuarioperfil'))
