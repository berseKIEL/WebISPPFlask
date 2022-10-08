class Config:
    SECRET_KEY = 'cualquiercosa1234'

class configuracionDesarrollo(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'isppf'
    MYSQL_PORT = 3306

config = {
    'desarrollo' : configuracionDesarrollo
}