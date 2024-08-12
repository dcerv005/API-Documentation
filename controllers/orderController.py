from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from marshmallow import ValidationError
from services import orderService
from caching import cache

def save():
    try:

        #Validate and deserialize input
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        order_save = orderService.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@cache.cached(timeout=60)    
def find_all():
    orders = orderService.find_all()
    return orders_schema.jsonify(orders), 200

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return orders_schema.jsonify(orderService.find_all_pagination(page=page, per_page=per_page)), 200