# Importación de Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

# Importación modular
from ....models.models import Perfil, Carpo, UsuarioPerfil,personal,personalcarpo,alumnocarpo,alumno,usuarioDatos, Usuario
from ....ext import db

# Desarrollo de la vista Bedel
bedel = Blueprint('bedel', __name__)

# @bedel.route('/')
# @login_required
# def cargar_carpos():
#     pass

# @bedel.route('/miscarreras', methods = ['GET','POST'])
# @login_required
# def mostrar_carreras_usuarioperfil():
#     carpo = Carpo.get_carpo_nombres(db)
#     if session['usuarioperfilactivo'] == 0:
#         return render_template('user/perfiles/añadircarpo.html', carpo = carpo)
#     else:
#         carpos = personalcarpo.cantcarpo(db,session['personalid'])
#         if len(carpos) >= 2:

#             return render_template('user/perfiles/listacarreras.html',carpo = carpo)
#         else:
#             carpoid = carpos[0][2]
#             carpo = Carpo.get_carpo_nombres_from_id(db,carpoid)
#             if carpo[2] == None:
#                 carpo = carpo[1]+' '+ carpo[3]
#             else:
#                 carpo = carpo[1]+' '+carpo[2]+' '+ carpo[3]


#             return render_template('user/perfiles/miscarreras.html',carpo = carpo)


#Funcionaaaaaaaaa
@bedel.route('/miscarreras', methods = ['GET','POST'])
@login_required
def mostrar_carreras_usuarioperfil():

    carpoTotales = Carpo.get_carpo_nombres(db)
    if session['usuarioperfilactivo'] == 0:
        
        return render_template('user/perfiles/bedel/añadircarpo.html', carpo = carpoTotales)
    else:
        listaCarpo = personalcarpo.cantcarpo(db, session['personalid'])
        carpoNombres = []
        
        for x in listaCarpo:
            carpoNombres.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
            
        print(carpoNombres)
        
        # Segundo se obtiene, los carpos que me falta inscribirme
        listaCarpoRestante = personalcarpo.get_carpoid_not_personalid(db, session['personalid'])
        carpoRestantes = []
        for x in listaCarpoRestante:
            carpoRestantes.append(Carpo.get_carpo_nombres_from_id(db,x[0]))
        
        print(carpoRestantes)
        # carpoid = personalcarpo.cantcarpo(db,session['personalid'])
        
        # carposUsuario=[]
        
        # for i in carpoid:
        #     carpo = Carpo.get_carpo_nombres_from_id(db,i)
        #     carposUsuario.append(carpo)
            
        # aux = []
        
        # for car in carpoTotales:
        #     for i in carpoid:
        #         print(car[0] , '=' , i[0])
        #         if(car[0] == i[0]):
        #             print(car[0] , '=' , i[0])
        #             aux.append(car)
                    
        # for a in aux:
        #     carpoTotales.remove(a)
            
        # print(carpoTotales)
            
        return render_template('user/perfiles/bedel/miscarreras.html',carposUsuario = carpoNombres, carpo = carpoRestantes)
    

@bedel.route('/DatosAcademicos')
@login_required
def mostrar_DatosAcademicos_usuarioperfil():
    return render_template('user/perfiles/DatosAcademicos.html')

@bedel.route('/activarperfil', methods = ['POST'])
@login_required
def activar_usuarioperfil():
    carpoid = request.form.get('Carpo')

    if personalcarpo.cargar_personalcarpo(db,session['personalid'], carpoid)[0]:
        UsuarioPerfil.activate_user_perfil(db, current_user.id, session['perfilid'])
        session['usuarioperfilactivo'] = 1

    return redirect(url_for('bedel.mostrar_carreras_usuarioperfil'))
    

@bedel.route('/agregarcarrera', methods = ['POST'])
@login_required
def agregar_carrera():
    
    carpoid = request.form.get('Carpo')
    
    if (carpoid==None):
        flash('No puedes inscribirte sin seleccionar una carrera')    
    else:
        personalcarpo.cargar_personalcarpo(db,session['personalid'], carpoid)[0]
        
    return redirect(url_for('bedel.mostrar_carreras_usuarioperfil'))


@bedel.route('/crear_alumno', methods = ['POST'])
@login_required
def crear_alumno():
    carpoid = request.form.get('Carpo')
    dnialumn = request.form.get('dni')
    nombre = request.form.get('nombre')
    apellido = request.form.get('Apellido')
    if nombre == '' or apellido == '' or dnialumn == '':
        flash('Datos incompletos')
    else:
        car = Carpo.get_carpo_nombres_from_id(db,carpoid)
        if car[2] == None:
            name = car[1]+' '+car[3]    
        else:
            name = car[1]+' '+car[2]+' '+car[3]   

        usuarioid = Usuario.create_user(db,dnialumn)
        
        UsuarioPerfil.create_userperfil(db,usuarioid,7)
        
        usuarioDatos.insert_usuariodatos(db,usuarioid,nombre,apellido,name)
        
        flash('Usuario Guardado')
    return redirect(url_for('bedel.mostrar_alumnos'))



@bedel.route('/Eliminarcarrera', methods = ['GET'])
@login_required
def eliminar_carrera():
    carpoid = request.args.get('carpoid')
    
    personalcarpo.eliminar_personalcarpo(db,session['personalid'], carpoid)

    if len(personalcarpo.cantcarpo(db,session['personalid'])) == 0:
        UsuarioPerfil.deactivate_user_perfil(db, current_user.id, session['perfilid'])
        session['usuarioperfilactivo'] = 0

    return redirect(url_for('bedel.mostrar_carreras_usuarioperfil'))


@bedel.route('/administrar_usuarios', methods = ['POST','GET'])
@login_required
def mostrar_alumnos():

    carpoid = personalcarpo.cantcarpo(db,session['personalid'])
    
    carpos=[]
    
    alumnosid=[]
    for i in carpoid:
        carpos = alumnocarpo.get_alumno_from_alumnocarpo(db,i[0])
        
        for a in carpos:
            alumnosid.append([a[0],i[0]])


    usuariosperfilesid =[]
    for i in alumnosid:
        usuariosperfilesid.append([alumno.get_usuarioperfil_from_alumno(db,i[0]),i[1]])

    usuariosid = []
    for i in usuariosperfilesid:
        usuariousuarioperfil = UsuarioPerfil.get_usuarioid_from_usuarioperfil(db,i[0])
        usuariousuarioperfil.append(i[1])
        usuariosid.append(usuariousuarioperfil)
    
    nombreapellido = []
    user = []
    for i in usuariosid:
        
        user = list(usuarioDatos.get_Nombre_Apellido_from_usuariodatos(db,i[0]))

        alid = alumno.get_alumnoid_by_usuarioperfilid(db,i[1])
        user.append(alid)
        
        
        car = Carpo.get_carpo_nombres_from_id(db,i[2])

        
        if car[2] == None:
            name = car[1]+' '+car[3]    
        else:
            name = car[1]+' '+car[2]+' '+car[3]   

        user.append(name)
        user.append(i[0])

        nombreapellido.append(user)
        

    carpo = Carpo.get_carpo_nombres(db)

    return render_template('user/perfiles/bedel/adminusuarios.html',nombreapellido = nombreapellido, carpo = carpo)

@bedel.route('/resetearcontraseña/<usuarioid>', methods = ['GET'])
@login_required
def resetear_contraseña(usuarioid):
    print(usuarioid, 'usuario')
    # Usuario.resetear_contraseña(db,usuarioid)
    # flash('Usuario reseteado')
    return redirect(url_for('bedel.mostrar_alumnos'))

@bedel.route('/deshabilitarusuario/<usuarioid>', methods = ['GET'])
@login_required
def deshabilitarusuario(usuarioid):
    print(usuarioid, 'usuario')
    # Usuario.resetear_contraseña(db,usuarioid)
    # flash('Usuario reseteado')
    return redirect(url_for('bedel.mostrar_alumnos'))


@bedel.route('/carpo/', methods=['GET','POST'])
@login_required
def ingresar_carpo():
    print(request.args.get('id'))
    return render_template('user/perfiles/bedel/ingresarcarpo.html')