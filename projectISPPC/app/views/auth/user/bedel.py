# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import UsuarioPerfil
from ....ext import db

# Desarrollo de la vista Bedel
bedel = Blueprint('bedel', __name__)

@bedel.route('/')
def index():
    if request.method == 'GET':
        id = current_user.id
    
        usuario = UsuarioPerfil.get_usuarioperfil_via_userid(db, id)
        activo = usuario[3]
    
        if activo == 0:    
            UsuarioPerfil.activate_user_perfil(db,id)
            # return redirect(url_for('user.datosacademicos'))
        
    return render_template('user/roles/bedel/home.html', activo=activo)