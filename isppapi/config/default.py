SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
PROPAGATE_EXCEPTIONS = True

# Database configuration
#SQLALCHEMY_DATABASE_URI = 'sqlite:///dbispp.sqlite'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/DBISPP' # Se establece su conexión a la base de datos
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

ERROR_404_HELP = False
