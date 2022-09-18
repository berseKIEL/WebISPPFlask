'''
Se realiza la implementación de la Extensión marshmallow.
Esta permite que la serialización de los modelos de la base de datos sean facilitados
para reutilización de codigo, permitiendo convertilos en JSON.
'''

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

ma = Marshmallow()
migrate = Migrate()