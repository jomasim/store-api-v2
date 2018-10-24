from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from utils import env
from instance.api_config import api_config

api_blueprint = Blueprint("store-api", __name__, url_prefix='/api/v2')
jwt = JWTManager()

''' setting api config '''


def create_app(config_setting):
    app = Flask(__name__)
    app.config.from_object(api_config[config_setting])
    app.config['JWT_SECRET_KEY'] = env('JWT_SECRET')

    jwt.init_app(app)

    ''' setting api blueprint  '''
    api = Api(api_blueprint)

    app.register_blueprint(api_blueprint)

    return app
