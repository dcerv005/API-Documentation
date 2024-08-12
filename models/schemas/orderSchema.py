from schema import ma
from marshmallow import fields, validate

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=0))
    total_price = fields.Float(required=True, validate= validate.Range(min=0))

order_schema = OrderSchema()
orders_schema= OrderSchema(many=True)

