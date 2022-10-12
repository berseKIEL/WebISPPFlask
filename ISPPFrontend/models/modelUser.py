from asyncio.windows_events import NULL
from .entidades.usuario import User

class modeluser():

    @classmethod
    def login(self, mysql, user):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * FROM usuarios WHERE usuario = %s'
            cur.execute(sql,([user.usuario]))
            row = cur.fetchone()
            if row != None:
                contr=row[2]
                contrtemp = row[4]
                contr = User.checkpassword(contr, user.contraseña)
                if contrtemp != None:
                    contrtemp = User.checkpassword(contrtemp, user.contraseña)
                else:
                    contrtemp=False

                user = User(row[0],row[1],contr,row[5], row[3],contrtemp)
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def comprobaremail(self, mysql, user):
        
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT email, idusuario FROM usuarios WHERE email = \'{}\''.format(str(user.email)))
            row=cur.fetchone()
            ema=str(row[0])
            id=int(row[1])
            if user.email == ema:
                
                cur.execute('UPDATE usuarios SET contraseñatemp = %s WHERE idusuario = %s',(str(User.generarhash(user.contraseñatemp)), id))
                mysql.connection.commit()
                return True
            else:
                return False

        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def getbyid(self, mysql, id):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT idusuario, usuario, tipo, email FROM usuarios WHERE idusuario = %s'
            cur.execute(sql,([int(id)]))
            row = cur.fetchone()
            if row != None:
                return User(row[0],row[1], None, row[2], row[3], None)
            else:
                return None
     
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def borrartemp(self, mysql, id):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE usuarios SET contraseñatemp = NULL WHERE idusuario = %s'
            cur.execute(sql,([int(id)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def cambiarcontraseña(slef,mysql,id, contraseña):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE usuarios SET contraseña = %s WHERE idusuario = %s'
            cur.execute(sql,([User.generarhash(contraseña)],[int(id)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)