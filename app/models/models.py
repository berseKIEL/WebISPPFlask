from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# Reciclaje de codigo
'''
try:
    cur = mysql.connection.cursor()
    consulta = ("select * from y where x = %s")
    cur.execute(consulta, [(query)])
    return cur.fetchone()
except Exception as ex:
    print(ex)
    raise Exception(ex)
'''

class Usuario(UserMixin):
    def __init__(self, id=None, usuario=None, usuariocorreo=None, usuariocontraseña=None, usuariocontraseñatemp=False, usuarioestado=0):
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
    def get_usuario_id(self, mysql, iduser):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select * from usuario where usuarioid = %s")
            cur.execute(consulta, [(iduser)])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_usuario_email(self, mysql, user):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select * from usuario where usuariocorreo = %s")
            cur.execute(consulta, [(user.usuariocorreo)])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_usuario_correo(self, mysql, correo):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select usuariocorreo from usuario where usuariocorreo = %s")
            cur.execute(consulta, [(correo)])
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
                if row[5] == 0:
                    if str(temp) == str(user.usuariocontraseña):
                        temp = True
                        user = Usuario(row[0], row[1], row[2],
                                       row[3], temp, row[5])
                    else:
                        temp = False
                        user = Usuario(row[0], row[1], row[2],
                                       row[3], temp, row[5])
                    return user
                else:
                    if temp != None:
                        temp = True
                        user = Usuario(row[0], row[1], row[2],
                                       row[3], temp, row[5])
                    else:
                        temp = False
                        user = Usuario(row[0], row[1], row[2], Usuario.revisar_contraseña_hasheada(
                            row[3], user.usuariocontraseña), temp, row[5])
                    return user
            else:
                row = Usuario.get_usuario_email(mysql, user)
                if row != None:
                    user = Usuario(row[0], row[1], row[2], Usuario.revisar_contraseña_hasheada(
                        row[3], user.usuariocontraseña), row[4], row[5])
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
            consulta = (
                'UPDATE usuario SET UsuarioContraseñaTemp = NULL WHERE usuarioid = %s')
            cur.execute(consulta, [str(id)])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def update_temp_password_password(self, db, newpassword, correo):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuario SET UsuarioContraseñaTemp = %s WHERE usuariocorreo = %s')
            cur.execute(consulta, [(newpassword), str(correo)])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def update_password(self, db, password, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuario SET usuariocontraseña = %s WHERE usuarioid = %s')
            cur.execute(
                consulta, [Usuario.generar_contraseña_hasheada(password), id])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def update_email(self, db, email, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuario SET usuariocorreo = %s WHERE usuarioid = %s')
            cur.execute(consulta, [email, id])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def activate_user(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuario SET usuarioactivo = 1 WHERE usuarioid = %s')
            cur.execute(consulta, [(id)])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def deactivate_user(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuario SET usuarioactivo = 0 WHERE usuarioid = %s')
            cur.execute(consulta, [(id)])
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

    @classmethod
    def get_login_id(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = ("select * from usuario where usuarioid = %s")
            cur.execute(consulta, [(id)])
            row = cur.fetchone()
            if row != None:
                user = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                return user
            else:
                return None

        except Exception as ex:
            print(ex)
            raise Exception(ex)


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
            consulta = ("select * from perfil where perfilid = %s")
            cur.execute(consulta, [id])
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
            cur.execute(consulta, [id])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_perfilid_via_userid(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                "select perfilid from UsuarioPerfil where usuarioid = %s")
            cur.execute(consulta, [id])
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_count_usuarioperfil(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = ('select COUNT(UsuarioPerfilID) from UsuarioPerfil where usuarioid = %s')
            cur.execute(consulta, [id])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def activate_user_perfil(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuarioperfil SET usuarioperfilactivo = 1 WHERE usuarioid = %s')
            cur.execute(consulta, [(id)])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def deactivate_user_perfil(self, db, id):
        try:
            cur = db.connection.cursor()
            consulta = (
                'UPDATE usuarioperfil SET usuarioperfilactivo = 0 WHERE usuarioid = %s')
            cur.execute(consulta, [(id)])
            db.connection.commit()
            return cur.lastrowid
        except Exception as ex:
            print(ex)
            raise Exception(ex)


class UsuarioDatos():
    def __init__(self, id=None, UsuarioNombre=None, UsuarioApellido=None, UsuarioCUIL=None, UsuarioFechaNac=None, UsuarioSexoDNI=None):
        self.id = id
        self.UsuarioNombre = UsuarioNombre
        self.UsuarioApellido = UsuarioApellido
        self.UsuarioCUIL = UsuarioCUIL
        self.UsuarioFechaNac = UsuarioFechaNac
        self.UsuarioSexoDNI = UsuarioSexoDNI
        
    @classmethod
    def get_usuario_datos_id(self, mysql, id):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select * from usuariodatos where usuarioid = %s")
            cur.execute(consulta, [(id)])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)
        
    @classmethod
    def get_cuilfnac_id(self, mysql, id):
        try:
            cur = mysql.connection.cursor()
            consulta = ("select usuariocuil, usuariofechanac from usuariodatos where usuarioid = %s")
            cur.execute(consulta, [(id)])
            return cur.fetchone()
        except Exception as ex:
            print(ex)
            raise Exception(ex)