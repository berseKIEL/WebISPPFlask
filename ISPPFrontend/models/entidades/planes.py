class Planes():

    def __init__(self,planid=None, planNombre=None) -> None:
        self.planid=planid
        self.planNombre=planNombre
    

    def listarPlanesPorCarrera(mysql,idcarrera):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT p.PlanID,p.PlanNombre, carpo.CARPOID FROM plandeestudio p JOIN carpo ON p.PlanID = carpo.PlanDeEstudioID WHERE carreraID = %s'            
            cur.execute(sql,[idcarrera])
            planes = cur.fetchall()
            return planes
        except Exception as ex:
            raise Exception(ex)

    def listarPlanes(mysql):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT PlanNombre FROM plandeestudio '            
            cur.execute(sql)
            planes = cur.fetchall()
            return planes
        except Exception as ex:
            raise Exception(ex)

    def listarPlanesPorCarreraYOrientacion(mysql,idcarrera,idorientacion):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT p.PlanID,p.PlanNombre, carpo.CARPOID FROM plandeestudio p JOIN carpo ON p.PlanID = carpo.PlanDeEstudioID WHERE carreraID = %s AND orientacionID = %s'
            cur.execute(sql,[idcarrera,idorientacion])
            ori = cur.fetchall()
            return ori
        except Exception as ex:
            raise Exception(ex)

    
    def AgregarPlan(mysql,nombrePlan):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO plandeestudio(PlanNombre) VALUES (%s)'
            cur.execute(sql,[nombrePlan])
            mysql.connection.commit()
            
        except Exception as ex:
            raise Exception(ex)

    def obtenerID(mysql,nombrePlan):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT PlanID from plandeestudio WHERE PlanNombre=%s'
            cur.execute(sql,[nombrePlan])
            idPlan=cur.fetchone()
            if idPlan:
                return idPlan[0]
            else: 
                return "vacio"

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def nombreplan(self, mysql, car,ori):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT carreranombre from carrera WHERE carreraid=%s'
            cur.execute(sql,[car])
            car=cur.fetchone()
            
            nombre = car[0] + '/'
            
            sql='SELECT orientacionnombre from orientacion WHERE orientacionid=%s'
            cur.execute(sql,[ori])
            ori=cur.fetchone()
            if ori != None:
                nombre = nombre + ori[0] + '/'
            return nombre
        except Exception as ex:
            raise Exception(ex)
