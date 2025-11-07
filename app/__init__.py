from flask import Flask
from migrations.config import config_info
from migrations.config import db
from routers.product_router import product_router
from flask import redirect

def create_app():
    app = Flask(__name__, static_folder='public', template_folder='templates')
    app.config['JSON_AS_ASCII'] = False
    config_info(app)
    app.register_blueprint(product_router, url_prefix='/products')

    @app.route('/')
    def home():
        
        return redirect('/products')
    return app