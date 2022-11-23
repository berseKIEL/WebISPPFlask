# Importación Modular
from ...ext import db
from ...models.models import Usuario
from ...models.models import UsuarioPerfil
from ...models.models import Perfil
from ...func.randomizer import generar_contraseña_temp
from ...func.sendemail import email

# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user

# Desarrollo de la vista Login

auth = Blueprint('auth', __name__)

# Creación de la ruta login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
        
    if request.method == 'POST':
        # Obtener los Formularios del HTML
        usuario = request.form.get('Lcorreo')
        contrasenia = request.form.get('Lpassword')
        
        # Crear la Clase usuario
        user = Usuario(usuario=usuario, usuariocontraseña=contrasenia, usuariocorreo=usuario)
        
        # Retorno del Usuario obtenido
        RetornoUsuario = Usuario.return_queried_user(db, user)
        
        # Preguntar si el usuario retornado no es nulo
        if RetornoUsuario != None:
            
            if RetornoUsuario.usuariocontraseña or RetornoUsuario.usuariocontraseñatemp:
                
                login_user(RetornoUsuario) # Logear al Flask-Login
                
                # Si el usuario no esta activo, no tendrá contraseña ni correo
                if RetornoUsuario.usuarioestado == 0:
                    return redirect(url_for('auth.cambiar_correopass'))
                
                if RetornoUsuario.usuario != RetornoUsuario.usuariocontraseña:
                    Usuario.update_temp_password(db,RetornoUsuario.id)
                
                # Si el usuario posee una contraseña temporal, se realiza una redirección hacia cambiar contraseña
                if RetornoUsuario.usuariocontraseñatemp:
                    return redirect(url_for('auth.cambiar_contraseña'))
                
                return redirect(url_for('auth.verificar_roles'))
            else:
                flash('Contraseña Incorrecta', category='error')
        else:
            flash('Usuario Inexistente', category='error')

    return render_template("user/login/log_in.html")

@auth.route('/verificacionderoles',methods=['GET'])
@login_required
def verificar_roles():
    # Si tiene mas de dos roles
    # Redirecciono al html "selecciona tu rol"
    if current_user.is_authenticated:
        id = current_user.id
        countperfiles = UsuarioPerfil.get_count_usuarioperfil(db, id)[0]
        if countperfiles >= 2:
            return redirect(url_for('auth.seleccionar_perfil'))
        else:
            # Si tiene un rol,
            # Redirecciona a su html correspondiente de su rol
            
            perfilobtenido = UsuarioPerfil.get_perfilid_via_userid(db, id)[0][0]
            
            if perfilobtenido == 1:
                return redirect(url_for('auth.adminview'))
            elif perfilobtenido in [2, 3, 4, 6, 8]:
                return redirect(url_for('docente.index'))
            elif perfilobtenido == 5:
                return redirect(url_for('bedel.index'))
            elif perfilobtenido == 7:
                return redirect(url_for('alumno.index'))
    return jsonify({'Respuesta' : 'No se pudo realizar la redirección'})


@auth.route('/seleccionarperfil',methods=['GET','POST'])
@login_required
def seleccionar_perfil():
    if request.method == 'GET':
        id = current_user.id
        perfiles = UsuarioPerfil.get_perfilid_via_userid(db, id)
        perfilesid = []
        perfilnames = []
        
        for i in perfiles:
            perfilesid.append(i[0])

        for i in perfilesid:
            perfilname = Perfil.get_perfil_via_id(db, i)[0]
            perfilnames.append(perfilname)
        
    if request.method == 'POST':
        perfilobtenido = int(request.form.get('opcion'))
        if perfilobtenido == 1:
            return redirect(url_for('auth.adminview'))
        elif perfilobtenido in [2, 3, 4, 6, 8]:
            return redirect(url_for('docente.index'))
        elif perfilobtenido == 5:
            return redirect(url_for('bedel.index'))
        elif perfilobtenido == 7:
            return redirect(url_for('alumno.index'))                
    return render_template('user/seleccionarperfil.html', perfilnames = perfilnames)

@auth.route('/recuperarcontrasenia', methods = ['GET', 'POST'])
def recuperar_contraseña():
        #genreacion y envio de contraseña temporal
        if request.method == 'POST':
            mail = request.form.get('email')
            p = generar_contraseña_temp()
            user = Usuario(usuariocorreo=mail,usuariocontraseñatemp=p)
                        
            try:
                Usuario.get_usuario_email(db, user)
            except Exception as e:
                flash('Error a la hora de enviar el email')
                return redirect(url_for('auth.recuperar_contraseña'))
            
            Email = email(mail, p)

            Enviacion = email.enviarCorreo(Email)
            
            print(Enviacion)
            
            if Enviacion:
                flash('Email enviado')
                return redirect(url_for('auth.login'))
            else:
                flash('El Email es Invalido')
        return render_template('user/login/recuperar_contraseña.html')
   

# @auth.route('/recuperarcontrasenia', methods = ['GET', 'POST'])
# def recuperar_contraseña():
#         #genreacion y envio de contraseña temporal
#         if request.method == 'POST':
#             email = request.form.get('email')
#             p = generar_contraseña_temp()
#             print(p)
#             Usuario.update_temp_password_password(db,p,email)
#         return render_template('/login/recuperar_contraseña.html')
    

@auth.route('/cambiarcontraseña',methods = ['POST','GET'])
def cambiar_contraseña():
    if request.method == 'GET':
        if current_user.is_authenticated:
            id = current_user.id
            logout_user()
        else:
            flash('¡¡¡¡¡¡¡POR APRETAR F5 DONDE NO DEBIAS!!!!!!!!!!')
            return redirect(url_for('auth.login'))
    if request.method == 'POST':
        id = request.form.get('id')
        contraseña1 = request.form.get('password')
        contraseña2 = request.form.get('passwordconfirm')
        
        if contraseña1 == contraseña2:
            Usuario.update_password(db, contraseña1, id)
            
            # Inicio de sesión
            RetornoUsuario = Usuario.get_login_id(db,id)
            login_user(RetornoUsuario)
            flash('¡Correo y Contraseña establecidas correctamente!')
            return redirect(url_for('auth.verificar_roles'))
        else:
            flash('Las contraseñas no coinciden')
            return render_template('user/login/cambiarcontraseña.html', id=id)
        
    return render_template('user/login/cambiarcontraseña.html', id=id)
    
@auth.route('/habilitarusuario', methods=['POST','GET'])
def cambiar_correopass():
    if request.method == 'GET':
        if current_user.is_authenticated:
            id = current_user.id
            logout_user()
        else:
            flash('¡¡¡¡¡¡¡POR APRETAR F5 DONDE NO DEBIAS!!!!!!!!!!')
            return redirect(url_for('auth.login'))
    if request.method == 'POST':
        id = request.form.get('id')
        correo = request.form.get('correo')
        contraseña1 = request.form.get('password')
        contraseña2 = request.form.get('passwordconfirm')
        
        if not (Usuario.get_usuario_correo(db, correo)):
            if contraseña1 == contraseña2:
                Usuario.update_email(db, correo, id)
                Usuario.update_password(db, contraseña1, id)
                Usuario.update_temp_password(db,id)
                Usuario.activate_user(db,id)
                
                # Inicio de sesión
                RetornoUsuario = Usuario.get_login_id(db,id)
                login_user(RetornoUsuario)
                flash('¡Correo y Contraseña establecidas correctamente!')
                return redirect(url_for('auth.verificar_roles'))
            else:
                flash('Las contraseñas no coinciden')
                return render_template('user/login/cambiarcorreoypass.html', id=id)
        else:
            flash('Ya existe un correo con ese correo')
            return render_template('user/login/cambiarcorreoypass.html', id=id)    
        
    return render_template('user/login/cambiarcorreoypass.html', id=id)

# Creación de la ruta logout
@auth.route("/log-out")
@login_required
def logout():
    logout_user()
    flash('El usuario ha cerrado la sesión correctamente')
    return redirect(url_for("home.index"))

