class Carrera():
    def __init__(self, CarreraID,CarreraNombre) -> None:
        self.CarreraID = CarreraID
        self.CarreraNombre = CarreraNombre
        
    @classmethod
    def add_Carrera(self, mysql, CarreraNombre):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO Carrera(CarreraNombre) VALUES (%s)'
            cur.execute(sql,[CarreraNombre])
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Carrera_all(self, mysql):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * FROM Carrera'
            cur.execute(sql)
            Carrera = cur.fetchall()
            return Carrera
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Carrera_id(self, mysql, CarreraID):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT * from Carrera WHERE CarreraID=%s'
            cur.execute(sql,[CarreraID])
            Carrera=cur.fetchone()
            if Carrera:
                return Carrera
            else: 
                return "vacio"
            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def edit_Carrera(self, mysql, CarreraID, CarreraNombre):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE Carrera SET CarreraNombre = %s WHERE CarreraID = %s'
            cur.execute(sql,[CarreraNombre,CarreraID])
            mysql.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_Carrera(self, mysql, CarreraID):
        try:
            cur = mysql.connection.cursor()
            sql = 'delete from Carrera where CarreraID = %s'
            cur.execute(sql,([int(CarreraID)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)