class Materia:

    def __init__(self,idmateria=None,nombremateria=None,idcarpo=None,año=None,Tipo=None) -> None:
        
        self.idmateria=idmateria
        self.nombremateria=nombremateria
        self.idcarpo=idcarpo
        self.año=año
        self.Tipo=Tipo

    @classmethod
    def agregarMateria(self, mysql,nombreMateria, año, tipo, idcarpo):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO materia(nombremateria, año, tipo, idcarpo) VALUES (%s,%s,%s,%s)'
            cur.execute(sql,[nombreMateria, año, tipo, idcarpo])
            mysql.connection.commit()
            
        except Exception as ex:
            raise Exception(ex)

    def listarMaterias(mysql,idcarpo):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT m.idmateria,m.nombremateria,m.año,m.tipo FROM carpo c JOIN materia m ON c.CARPOID = m.idcarpo WHERE CARPOID = %s ORDER BY m.tipo ASC'
            cur.execute(sql,[idcarpo])
            materias = cur.fetchall()
            return materias
        except Exception as ex:
            raise Exception(ex)

    def cantidadDeAños(mysql,idcarpo):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT COUNT(DISTINCT(m.año)) FROM carpo c JOIN materia m ON c.CARPOID = m.idcarpo WHERE CARPOID = %s'            
            cur.execute(sql,[idcarpo])
            año = cur.fetchone()
            año=año[0]
            return año
        except Exception as ex:
            raise Exception(ex)

    

    