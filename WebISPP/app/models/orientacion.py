class Orientacion():
    def __init__(self, OrientacionID,OrientacionNombre) -> None:
        self.OrientacionID = OrientacionID
        self.OrientacionNombre = OrientacionNombre
        
    @classmethod
    def add_Orientacion(self, mysql, OrientacionNombre):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO Orientacion(OrientacionNombre) VALUES (%s)'
            cur.execute(sql,[OrientacionNombre])
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Orientacion_all(self, mysql):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * FROM Orientacion'
            cur.execute(sql)
            Orientacion = cur.fetchall()
            return Orientacion
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Orientacion_id(self, mysql, OrientacionID):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT * from Orientacion WHERE OrientacionID=%s'
            cur.execute(sql,[OrientacionID])
            Orientacion=cur.fetchone()
            if Orientacion:
                return Orientacion
            else: 
                return "vacio"
            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def edit_Orientacion(self, mysql, OrientacionID, OrientacionNombre):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE Orientacion SET OrientacionNombre = %s WHERE OrientacionID = %s'
            cur.execute(sql,[OrientacionNombre,OrientacionID])
            mysql.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_Orientacion(self, mysql, OrientacionID):
        try:
            cur = mysql.connection.cursor()
            sql = 'delete from Orientacion where OrientacionID = %s'
            cur.execute(sql,([int(OrientacionID)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)