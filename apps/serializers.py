from marshmallow_mongoengine import ModelSchema
from marshmallow_mongoengine import fields as fd
from .models import Table, Field, DIYApp


class TableSchema(ModelSchema):
    fields = fd.Nested("FieldSchema", many=True)

    class Meta:
        model_skip_values = ()
        model = Table


class SubmitTableSchema(TableSchema):
    table_name = fd.String(required=True, load_only=True, attribute="name")
    verbose_name = fd.String(required=True, load_only=True, attribute="verbose")
    field = fd.Nested("FieldSchema", many=True, attribute="fields")


class FieldSchema(ModelSchema):
    class Meta:
        model_skip_values = ()
        model = Field


class DIYAppSchema(ModelSchema):
    app_id = fd.String(required=True)
    table_list = fd.Nested("TableSchema", many=True)

    class Meta:
        model_skip_values = ()
        model = DIYApp