import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="dbispp"
)
cur = db.cursor()

consulta = ('select alumnoid from alumno where usuarioperfilid = 3')
consulta = ('select carpoid from alumnocarpo where alumnoid = 1 order by carpoid')

cur.execute(consulta)

for x in cur.fetchall():
    print(x)