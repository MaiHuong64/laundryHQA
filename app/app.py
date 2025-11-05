from flask import Flask
from migrations.config import config_info
from migrations.config import db
from routers.product_router import product_router

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    config_info(app)

    @app.route('/')
    def home():
        return "Welcome to the Invoice Management System"
    app.register_blueprint(product_router, url_prefix='/products')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
