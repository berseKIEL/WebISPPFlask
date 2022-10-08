from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id=None, usuario=None, contraseña=None, tipo=None, email=None, contraseñatemp = False, nombre = None, apellido = None) -> None:
        self.id = id
        self.usuario = usuario
        self.contraseña = contraseña
        self.tipo = tipo
        self.email = email
        self.contraseñatemp = contraseñatemp
    
    @classmethod
    def checkpassword(self, hash, contraseña):
        return check_password_hash(hash,contraseña)

    @classmethod
    def generarhash(self, contraseña):
        return generate_password_hash(contraseña)