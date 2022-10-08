class Carpo():

    def __init__(self, CARPOID=None,CarreraID=None,PlanDeEstudioID=None,OrientacionID=None,CarpoPrograma=None) -> None:
        self.CARPOID=CARPOID
        self.CarreraID=CarreraID
        self.PlanDeEstudioID=PlanDeEstudioID
        self.OrientacionID=OrientacionID
        self.CarpoPrograma=CarpoPrograma
        
    @classmethod    
    def AgregarCarpo(self,mysql,idCarr,idOri,idPlan):
        try:
            cur=mysql.connection.cursor()
            if idOri=="Null":
                sql='INSERT INTO carpo(CarreraID,PlanDeEstudioID) VALUES (%s,%s)'
                cur.execute(sql,[idCarr,idPlan])
            else:
                sql='INSERT INTO carpo(CarreraID,OrientacionID,PlanDeEstudioID) VALUES (%s,%s,%s)'
                cur.execute(sql,[idCarr,idOri,idPlan])
            mysql.connection.commit()
            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def buscarcarpo(self, mysql, idcar,idori,idplan):
        try:
            cur=mysql.connection.cursor()
            if idori=="-1":
                sql='SELECT carpoid FROM carpo WHERE carreraid = %s AND plandeestudioid = %s'
                cur.execute(sql,[idcar,idplan])
            else:
                sql = 'Select carpoid from carpo where carreraid = %s and plandeestudioid = %s and orientacionid = %s'
                cur.execute(sql,[idcar,idplan,idori])
            idcarpo = cur.fetchone()
            return idcarpo[0]


        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def nombreCarpo(self,mysql,idcarpo):
        try:
            cur=mysql.connection.cursor()
            sql='''SELECT CarreraNombre, OrientacionNombre, PlanNombre
FROM (((carpo AS C left join carrera AS car ON C.CarreraID = car.CarreraID) 
	  inner join plandeestudio AS P ON C.PlanDeEstudioID = P.PlanID)
      LEFT join orientacion AS ori ON C.OrientacionID = ori.OrientacionID)
WHERE C.CARPOID = %s;'''
            cur.execute(sql,[idcarpo])
            nombre = cur.fetchone()
            return nombre 

        except Exception as ex:
            raise Exception(ex)

    