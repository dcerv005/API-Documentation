from flask import jsonify, request
from models.schemas.employeeSchema import employee_schema, employees_schema
from marshmallow import ValidationError
from services import employeeService
from caching import cache


def save():
    try:
        employee_data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        employee_save = employeeService.save(employee_data)
        return employee_schema.jsonify(employee_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@cache.cached(timeout=60)
def find_all():
    employees = employeeService.find_all()
    return employees_schema.jsonify(employees), 200