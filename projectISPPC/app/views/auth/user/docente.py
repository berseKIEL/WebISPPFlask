# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import UsuarioDatos, Perfil
from ....ext import db

# Desarrollo de la vista docente
docente = Blueprint('docente', __name__)

@docente.route('/')
@login_required
def index():
    # Obtener el perfil que es
    perfilid = 0
    
    if session['perfilid']:
        perfilid=session['perfilid']
        
    perfil = Perfil.get_perfil_via_id(db, perfilid)[0][1]
    consulta = UsuarioDatos.get_usuario_datos_id(db, current_user.id)
    
    return render_template('user/home.html', perfil=perfil, consulta=consulta)