class Materia():
    def __init__(self, MateriaID, MateriaNombre, MateriaAño, MateriaTipo, CarpoIDMat) -> None:
        self.MateriaID = MateriaID
        self.MateriaNombre = MateriaNombre
        self.MateriaAño = MateriaAño
        self.MateriaTipo = MateriaTipo
        self.CarpoIDMat = CarpoIDMat

    @classmethod
    def add_Materia(self, mysql, MateriaNombre, MateriaAño, MateriaTipo, CarpoIDMat):
        try:
            cur = mysql.connection.cursor()
            sql = 'INSERT INTO Materia(MateriaNombre, MateriaAño, MateriaTipo,CarpoIDMat) VALUES (%s, %s, %s,%s)'
            cur.execute(sql, [MateriaNombre, MateriaAño, MateriaTipo, CarpoIDMat])
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_Materia_all(self, mysql, CarpoIDMat):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT materiaid,MateriaNombre, Materiaaño, materiatipo FROM Materia where CarpoIDMat = %s ORDER BY MateriaTipo ASC'
            cur.execute(sql,[CarpoIDMat])
            Materia = cur.fetchall()
            return Materia
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_Materia_id(self, mysql, MateriaID):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * from Materia WHERE MateriaID=%s'
            cur.execute(sql, [MateriaID])
            Materia = cur.fetchone()
            if Materia:
                return Materia
            else:
                return "vacio"

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def edit_Materia(self, mysql, MateriaID, MateriaNombre, MateriaAño, MateriaTipo):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE Materia SET MateriaNombre = %s, MateriaAño = %s, MateriaTipo = %s WHERE MateriaID = %s'
            cur.execute(sql, [MateriaNombre, MateriaAño,
                        MateriaTipo, MateriaID])
            mysql.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_Materia(self, mysql, MateriaID):
        try:
            cur = mysql.connection.cursor()
            sql = 'delete from Materia where MateriaID = %s'
            cur.execute(sql, ([int(MateriaID)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def cantidadDeAños(self, mysql,idcarpo):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT COUNT(DISTINCT(m.MateriaAño)) FROM carpo c JOIN materia m ON c.CARPOID = m.carpoidmat WHERE CARPOID = %s'            
            cur.execute(sql,[idcarpo])
            año = cur.fetchone()
            año=año[0]
            return año
        except Exception as ex:
            raise Exception(ex)