from flask import jsonify, request
from models.schemas.productionSchema import production_schema, productions_schema
from marshmallow import ValidationError
from services import productionService
from caching import cache


def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        production_save = productionService.save(production_data)
        return production_schema.jsonify(production_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@cache.cached(timeout=60)
def find_all():
    productions = productionService.find_all()
    return productions_schema.jsonify(productions), 200