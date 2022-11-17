from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

cors = CORS()

db = MySQL()

csrf = CSRFProtect()