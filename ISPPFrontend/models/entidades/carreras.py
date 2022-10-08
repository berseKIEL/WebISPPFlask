
from queue import Empty


class Carreras():

    def __init__(self, idcarrera=None, nombrecarrera=None) -> None:
        self.idcarrera=idcarrera
        self.nombrecarrera=nombrecarrera

    def listarCarreras(mysql):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * FROM carrera'
            cur.execute(sql)
            carrera = cur.fetchall()
            return carrera
        except Exception as ex:
            raise Exception(ex)

    def borrarCarreras(mysql,idCarrera):
        try:
            cur = mysql.connection.cursor()
            sql = 'delete from carrera where idCarrera = %s'
            cur.execute(sql,([int(idCarrera)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    def buscarCarreraPorNombre(mysql,nombre):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * FROM producto WHERE CarreraNombre LIKE %s'
            cur.execute(sql,(nombre))
            prod = cur.fetchone()
            if prod!=None:
                return prod
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    def AgregarCarrera(mysql,nombreCarr):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO carrera(CarreraNombre) VALUES (%s)'
            cur.execute(sql,[nombreCarr])
            mysql.connection.commit()
            
        except Exception as ex:
            raise Exception(ex)

    def obtenerID(mysql,nombreCarr):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT CarreraID from carrera WHERE CarreraNombre=%s'
            cur.execute(sql,[nombreCarr])
            idCarr=cur.fetchone()
            if idCarr:
                return idCarr[0]
            else: 
                return "vacio"
            
        except Exception as ex:
            raise Exception(ex)

    def editarCarrera(mysql,nombreOriginal,nombreCambio):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE carrera SET CarreraNombre = %s WHERE CarreraNombre LIKE %s'
            cur.execute(sql,[nombreCambio,nombreOriginal])
            mysql.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)