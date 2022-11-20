from flask_mysqldb import MySQL
from flask_login import LoginManager
from flask_mail import Mail

db = MySQL()
LogMan = LoginManager()
mail = Mail()