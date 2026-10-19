from flask import Flask
from .routes import routes

def create_app():
    # Le decimos explícitamente que la carpeta static y templates están dentro de app
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config['SECRET_KEY'] = 'clave-secreta'
    
    app.register_blueprint(routes)
    
    return app


    