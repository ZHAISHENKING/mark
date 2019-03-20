from admin import db
from utils.constant import FIELD_CHOICE
import time


class UrlConfig(db.Document):
    """
    url配置
    """
    name = db.StringField(verbose_name="接口名称")
    prefix = db.StringField(verbose_name="协议")
    host = db.StringField(verbose_name="域名")
    api = db.StringField(verbose_name="接口地址")
    create_at = db.IntField(verbose_name="创建时间")


class Mark(db.Document):
    """
    mark
    """
    title = db.StringField(verbose_name='标题')
    method = db.StringField(verbose_name="方法")
    func = db.StringField(verbose_name="功能")
    url = db.ReferenceField(UrlConfig, verbose_name='路由', reverse_delete_rule=2)
    path = db.StringField()
    input = db.StringField()
    output = db.StringField()
    err_output = db.StringField()
    create_at = db.IntField(default=int(time.time()))


class Table(db.Document):
    """
    table
    """
    name = db.StringField()
    verbose = db.StringField(verbose_name="别名")
    fields = db.ListField(db.ReferenceField("Field"), verbose_name="字段")


class Field(db.Document):
    """
    字段
    """
    name = db.StringField(verbose_name="字段名")
    verbose = db.StringField(verbose_name='别名')
    field_type = db.IntField(choice=FIELD_CHOICE, verbose_name="字段类型")
    fk_table = db.StringField(verbose_name="关联表")
    many = db.BooleanField(verbose_name="多对多")


class DIYApp(db.Document):
    """
    app
    """
    name = db.StringField()
    table_list = db.ListField(db.ReferenceField("Table"), verbose_name="表格")