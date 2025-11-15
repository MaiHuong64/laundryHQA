from flask import Flask
from migrations.config import config_info
from models.product import Product
from models.customer import Customer
from routers.product_router import product_router
from routers.custome_router import customer_router
from flask import render_template

def create_app():
    app = Flask(__name__, static_folder='public', template_folder='templates')
    app.config['JSON_AS_ASCII'] = False
    config_info(app)

    app.register_blueprint(product_router, url_prefix='/api/products')
    app.register_blueprint(customer_router, url_prefix='/api/customers')
    
    
    @app.route('/')
    def home():
        return  render_template('index.html')

    # Trang quản lý sản phẩm (frontend)
    @app.route('/product')
    def product():
        products =  Product.query.all()
        return render_template('product.html', products=products)       
    
    @app.route('/customer')
    def customer():
        customers =  Customer.query.all()
        return render_template('customer.html', customers=customers)       
    
    @app.route('/invoice')
    def invoice():
        invoices =  Product.query.all()
        return render_template('invoice.html', invoices=invoices)       
    return app