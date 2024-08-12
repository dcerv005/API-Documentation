from flask import Blueprint
from controllers.userController import login, save

user_blueprint= Blueprint('user_bp', __name__)
user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/login', methods=['POST'])(login)