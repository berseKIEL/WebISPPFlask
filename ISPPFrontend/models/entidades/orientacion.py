class Orientacion():

    def __init__(self,OrientacionID=None, OrientacionNombre=None) -> None:
        self.OrientacionID=OrientacionID
        self.OrientacionNombre=OrientacionNombre

    
    def listarOrientaciones(mysql):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT OrientacionNombre FROM orientacion'            
            cur.execute(sql)
            orientacion = cur.fetchall()
            return orientacion
        except Exception as ex:
            raise Exception(ex)

    def listarOrientacionPorCarrera(mysql,idcarrera):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT orientacion.OrientacionID,orientacion.OrientacionNombre FROM carrera JOIN carpo ON carrera.carreraID= carpo.carreraID JOIN orientacion ON orientacion.OrientacionID = carpo.OrientacionID WHERE carrera.carreraID=%s'
            cur.execute(sql,[idcarrera])
            ori = cur.fetchall()
            if len(ori)==0:
                ori=None
            return ori
        except Exception as ex:
            raise Exception(ex)

    def AgregarOrientacion(mysql,nombreOri):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO orientacion(OrientacionNombre) VALUES (%s)'
            cur.execute(sql,[nombreOri])
            mysql.connection.commit()

        except Exception as ex:
            raise Exception(ex)

    def obtenerID(mysql,nombreOri):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT OrientacionID from orientacion WHERE OrientacionNombre=%s'
            cur.execute(sql,[nombreOri])
            idOri=cur.fetchone()
            if idOri:
                return idOri[0]
            else: 
                return "vacio"

        except Exception as ex:
            raise Exception(ex)