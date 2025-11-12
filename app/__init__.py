from flask import Flask
from migrations.config import config_info
from migrations.config import db
from routers.product_router import product_router
from flask import redirect, render_template

def create_app():
    app = Flask(__name__, static_folder='public', template_folder='templates')
    app.config['JSON_AS_ASCII'] = False
    config_info(app)
    app.register_blueprint(product_router, url_prefix='/api/products')

    @app.route('/')
    def home():
        return  render_template('customer.html')

    # Trang quản lý sản phẩm (frontend)
    @app.route('/product')
    def product():
        return render_template('product.html')       
    return app