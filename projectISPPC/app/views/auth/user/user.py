# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import UsuarioDatos, Perfil, UsuarioPerfil
from ....ext import db

# Desarrollo de la vista usuario
usuario = Blueprint('user', __name__)


@usuario.route('/')
@login_required
def index():
    # Obtener el perfil que es
    perfilid = 0

    if session['perfilid']:
        perfilid = session['perfilid']

    perfil = Perfil.get_perfil_via_id(db, perfilid)[0][1]
    consulta = UsuarioDatos.get_usuario_datos_id(db, current_user.id)
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
