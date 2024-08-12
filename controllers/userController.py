from flask import request, jsonify
from models.schemas.userSchema import Users_schema, User_schema
from services import userService
from marshmallow import ValidationError
from utils.util import token_required, role_required
def login():
    users = request.json
    user = userService.login_customer(users['username'], users['password'])
    if user:
        return jsonify(user), 200
    
    else: 
        resp = {
            'status' : 'Error',
            'message' : 'User does not exist'
        }
        return jsonify(resp), 404

@role_required('admin')    
def save():
    #POST request. /customers POST contain JSON
    try:
       user_data = User_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user_save = userService.save(user_data)
    if user_save is not None:
        return User_schema.jsonify(user_save), 201
    else: 
        return jsonify({"message":"Fallback method error activated", "body":user_data}), 400