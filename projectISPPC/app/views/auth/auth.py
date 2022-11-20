# Importación Modular
from ...ext import db
from ...models.models import Usuario
from ...func.randomizer import generar_contraseña_temp
from ...func.sendemail import email

# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

# Desarrollo de la vista Login

auth = Blueprint('auth', __name__)

# Creación de la ruta login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los Formularios del HTML
        usuario = request.form.get('Lcorreo')
        contrasenia = request.form.get('password')
        
        # Crear la Clase usuario
        user = Usuario(usuario=usuario, usuariocontraseña=contrasenia, usuariocorreo=usuario)
        print(user.usuario)
        
        # Retorno del Usuario obtenido
        RetornoUsuario = Usuario.return_queried_user(db, user)
                
        # Preguntar si el usuario retornado no es nulo
        if RetornoUsuario != None:
            if RetornoUsuario.contraseña or RetornoUsuario.contraseñatemp:
                
                login_user(RetornoUsuario) # Logear al Flask-Login
                
                if RetornoUsuario.usuario != RetornoUsuario.usuariocontraseña:
                    Usuario.update_temp_password(RetornoUsuario.id)
                
                # Si el usuario no esta activo, no tendrá contraseña ni correo
                if RetornoUsuario.usuarioestado == 0:
                    return redirect(url_for('auth.cambiar_correopass'))
                
                # Si el usuario posee una contraseña temporal, se realiza una redirección hacia cambiar contraseña
                if RetornoUsuario.contraseñatemp:
                    return redirect(url_for('auth.cambiar_contraseña'))
                
                return redirect(url_for('views.home'))
            else:
                flash('Contraseña Incorrecta', category='error')
        else:
            flash('Usuario Inexistente', category='error')

    return render_template("login/log_in.html")

@auth.route('/recuperarcontrasenia', methods = ['GET', 'POST'])
def recuperar_contraseña():
        #genreacion y envio de contraseña temporal
        if request.method == 'POST':
            mail = request.form.get('email')
            p = generar_contraseña_temp()
            user = Usuario(email=mail,contraseñatemp=p)
            
            print(user.contraseñatemp)
            
            try:
                Usuario.get_usuario_email(db, user)
            except Exception as e:
                flash('Error a la hora de enviar el email')
                return redirect(url_for('auth.recuperar_contraseña'))
            
            Email = email(db, mail, p)
            Enviacion = email.enviarCorreo(Email)
            print(Enviacion)
            if Enviacion:
                flash('Email enviado')
                return redirect(url_for('auth.login'))
            else:
                flash('El Email es Invalido')
        return render_template('/login/recuperar_contraseña.html')
    

@auth.route('/cambiarcontraseña',methods = ['POST','GET'])
def cambiar_contraseña():
    if request.method == 'GET':
        id = current_user.id
        logout_user() 
    #confirma si la nueva clave es correcta y la guarda
    if request.method == 'POST':
        id = request.form.get('id')
        contraseña1 = request.form.get('password')
        contraseña2 = request.form.get('passwordconfirm')
        if contraseña1 == contraseña2:
            try: 
                cur = db.connection.cursor()
                consulta = ('UPDATE usuarios SET contraseña = %s WHERE idusuario = %s')
                cur.execute(consulta,[Usuario.generarhash(contraseña1), id])
                db.connection.commit()
                flash('Contraseña cambiada correctamente')
                return redirect(url_for('views.index'))
            except Exception as ex:
                flash('No se pudo realizar la consulta SQL', ex)
                print(ex)
                return render_template('cambiarcontraseña.html', id=id)
        else:
            flash('Las contraseñas no coinciden')
            return render_template('cambiarcontraseña.html', id=id)
    return render_template('cambiarcontraseña.html', id=id)
    
@auth.route('/asd1', methods=['POST','GET'])
def cambiar_correopass():
    return '<h1> Cambiar contraseña y cambiar correo<h1>'

# Creación de la ruta logout
@auth.route("/log-out")
@login_required
def logout():
    logout_user()
    flash('El usuario ha cerrado la sesión correctamente')
    return redirect(url_for("views.index"))