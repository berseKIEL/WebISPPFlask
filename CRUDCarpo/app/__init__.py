from flask import Flask

from .ext import cors, db, csrf

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    
    db.init_app(app)
    cors.init_app(app)
    csrf.init_app(app)
    

    from .views.views import vistas
    
    from .views.crudcarpo import crudcarpo
    
    app.register_blueprint(vistas)
    app.register_blueprint(crudcarpo)

    return app
