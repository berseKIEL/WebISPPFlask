class Plan():
    def __init__(self, PlanID,PlanNombre) -> None:
        self.PlanID = PlanID
        self.PlanNombre = PlanNombre
        
    @classmethod
    def add_Plan(self, mysql, PlanNombre):
        try:
            cur=mysql.connection.cursor()
            sql='INSERT INTO Plan(PlanNombre) VALUES (%s)'
            cur.execute(sql,[PlanNombre])
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Plan_all(self, mysql):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT * FROM Plan'
            cur.execute(sql)
            Plan = cur.fetchall()
            return Plan
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Plan_id(self, mysql, PlanID):
        try:
            cur=mysql.connection.cursor()
            sql='SELECT * from Plan WHERE PlanID=%s'
            cur.execute(sql,[PlanID])
            Plan=cur.fetchone()
            if Plan:
                return Plan
            else: 
                return "vacio"
            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def edit_Plan(self, mysql, PlanID, PlanNombre):
        try:
            cur = mysql.connection.cursor()
            sql = 'UPDATE Plan SET PlanNombre = %s WHERE PlanID = %s'
            cur.execute(sql,[PlanNombre,PlanID])
            mysql.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_Plan(self, mysql, PlanID):
        try:
            cur = mysql.connection.cursor()
            sql = 'delete from Plan where PlanID = %s'
            cur.execute(sql,([int(PlanID)]))
            mysql.connection.commit()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_plan_via_oricar(self, mysql,carreraid,orientacionid):
        try:
            cur = mysql.connection.cursor()
            sql = 'SELECT p.PlanID,p.PlanNombre, carpo.CARPOID FROM plandeestudio p JOIN carpo ON p.PlanID = carpo.PlanDeEstudioID WHERE carreraID = %s AND orientacionID = %s'
            cur.execute(sql,[carreraid,orientacionid])
            ori = cur.fetchall()
            return ori
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_plan_via_car(self,mysql,carreraid):
        try:
            cur = mysql.connection.cursor()
            sql='SELECT p.PlanID,p.PlanNombre, carpo.CARPOID FROM plandeestudio p JOIN carpo ON p.PlanID = carpo.PlanDeEstudioID WHERE carreraID = %s'            
            cur.execute(sql,[carreraid])
            planes = cur.fetchall()
            return planes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_nombre_ori_plan(self, mysql, car,ori):
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