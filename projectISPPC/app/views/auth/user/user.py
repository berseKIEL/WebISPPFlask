# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_required, current_user

# Importación modular
from ....models.models import Perfil, UsuarioPerfil
from ....ext import db

# Desarrollo de la vista usuario
usuario = Blueprint('user', __name__)

@usuario.route('/')
@login_required
def habilitar_usuario_firstlogin():
    return render_template('user/habilitar_first_login_dos.html')

@usuario.route('/obtenernombredelperfil')
@login_required
def obtener_nombre_perfil():
    perfilid = 0
    
    if session['perfilid']:
        perfilid=session['perfilid']
        
    perfiles = Perfil.get_perfil_via_id(db, perfilid)[0][1]
    return jsonify({'Respuesta':perfiles})


@usuario.route('/obtenercountperfil')
@login_required
def obtener_count_perfiles():
    perfiles = UsuarioPerfil.get_count_usuarioperfil(db, current_user.id)[0]
    return jsonify({'Respuesta':perfiles})