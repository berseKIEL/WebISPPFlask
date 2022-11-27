# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

# Desarrollo de la vista Login

usuario = Blueprint('user', __name__)

@usuario.route('/')
@login_required
def habilitar_usuario_firstlogin():
    if request.method == 'GET':
        if current_user.usuarioestado == 1:
            return redirect
    return render_template('user/habilitar_first_login_dos.html')