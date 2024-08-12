from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from caching import cache
from werkzeug.security import generate_password_hash
from flask_cors import CORS

from models.customer import Customer
from models.employee import Employee
from models.order import Order
from models.product import Product
from models.production import Production


from routes.customerBP import customer_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.employeeBP import employee_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs' #URL for exposing Swagger UI (without trailing'/')
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Factory Management System API"
    }
)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    CORS(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    # /customers
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def configure_rate_limit():
    limiter.limit("5 per day")(customer_blueprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfigAssignment')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)