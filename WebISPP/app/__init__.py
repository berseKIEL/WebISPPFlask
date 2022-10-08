from flask import Flask

from flask_cors import CORS

import requests

import os

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    CORS(app)

    from .views.views import vistas
    
    from .views.crudcarpo import crudcarpo
    
    app.register_blueprint(vistas)
    app.register_blueprint(crudcarpo)

    return app
