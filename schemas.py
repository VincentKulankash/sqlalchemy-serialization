from marshmallow import fields, validate 
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Product, Category

class CategorySchema(SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=80))

    class Meta:
        model= Category
        load_instance=True
        include_relationships=False

class ProductSchema(SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=120))
    price = fields.Decimal(required=True, as_string=True)

    category_id = fields.Integer(required=True)
    
    category = fields.Nested(CategorySchema, dump_only=True)


    class Meta:
        model = Product
        load_instance=True
        include_fk=True

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)