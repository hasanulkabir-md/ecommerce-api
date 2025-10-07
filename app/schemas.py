from marshmallow import Schema, fields, validate


class UserSchema(Schema):
id = fields.Int(dump_only=True)
email = fields.Email(required=True)
name = fields.Str(required=True)
role = fields.Str()


class ProductCreateSchema(Schema):
title = fields.Str(required=True, validate=validate.Length(min=1))
description = fields.Str()
price = fields.Float(required=True)
stock = fields.Int(required=True)


class ProductSchema(ProductCreateSchema):
id = fields.Int(dump_only=True)


class CartItemSchema(Schema):
product_id = fields.Int(required=True)
qty = fields.Int(required=True, validate=validate.Range(min=1))


class CartSchema(Schema):
items = fields.List(fields.Nested({
"product_id": fields.Int(),
"title": fields.Str(),
"unit_price": fields.Float(),
"qty": fields.Int(),
"line_total": fields.Float()
}))
total = fields.Float()


class OrderSchema(Schema):
id = fields.Int()
total = fields.Float()
created_at = fields.DateTime()
items = fields.List(fields.Nested({
"product_id": fields.Int(),
"title": fields.Str(),
"unit_price": fields.Float(),
"qty": fields.Int()
}))