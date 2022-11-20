from ..ext import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(UserMixin):
    def __init__(self, id=None, usuario=None, usuariocorreo=None, usuariocontraseña=None, usuariocontraseñatemp=None, usuarioestado=0):
        self.id = id
        self.usuario = usuario
        self.usuariocorreo = usuariocorreo
        self.usuariocontraseña = usuariocontraseña
        self.usuariocontraseñatemp = usuariocontraseñatemp
        self.usuarioestado = usuarioestado

    @classmethod
    def get_usuario_DNI(self, mysql, user):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select * from usuario where usuario = %s")
            cur.execute(consulta, [(user.usuario)])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_usuario_email(self, mysql, user):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select * from usuario where usuariocorreo = %s")
            cur.execute(consulta, [str(user.usuariocorreo)])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def return_queried_user(self, mysql, user):
        try:
            row = Usuario.get_usuario_DNI(mysql, user)
            if row != None:
                temp = row[4]
                if temp != None:
                    temp = Usuario.revisar_contraseña_hasheada(temp, user.usuariocontraseña)
                else:
                    temp = False
                user = Usuario(row[0], row[1], row[2], Usuario.checkpassword(
                    row[3], user.contraseña), temp, row[5])
                return user
            else:
                row = Usuario.get_usuario_email(mysql, user)
                if row != None:
                    user = Usuario(row[0], row[1], row[2], Usuario.checkpassword(row[3], user.contraseña), row[4], row[5])
                    return user
                else:
                    return None
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def update_temp_password(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = ('UPDATE usuarios SET UsuarioContraseñaTemp = NULL WHERE idusuario = %s')
            cur.execute(consulta, (str(id)))
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)
        
    @classmethod
    def update_password(self, db,password, id):
        try:
            cur = db.connection.cursor()
            consulta = ('UPDATE usuarios SET contraseña = %s WHERE idusuario = %s')
            cur.execute(consulta, [(password, id)])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def revisar_contraseña_hasheada(self, hash, contraseña):
        return check_password_hash(hash, contraseña)

    @classmethod
    def generar_contraseña_hasheada(self, contraseña):
        return generate_password_hash(contraseña)

class Perfil():
    def __init__(self, id=None, perfil=None):
        self.id = id
        self.perfil = perfil
    
    @classmethod
    def get_all_perfiles(self, db):
        try:
            cur = db.connection.cursor()
            consulta = ("select * from perfil")
            cur.execute(consulta)
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            raise Exception(ex)
        
    @classmethod
    def get_perfil_via_id(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = ("select perfil from perfil where perfilid = %s")
            cur.execute(consulta,[id])
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            raise Exception(ex)
    

class UsuarioPerfil():
    def __init__(self, id=None, perfilid=None, usuarioid=None, usuarioperfilactivo=0):
        self.id = id
        self.perfilid = perfilid
        self.usuarioid = usuarioid
        self.usuarioperfilactivo = usuarioperfilactivo
    
    @classmethod
    def get_usuarioperfil_via_userid(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = ("select * from UsuarioPerfil where usuarioid = %s")
            cur.execute(consulta,[id])
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            raise Exception(ex)