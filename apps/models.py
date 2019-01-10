from admin import db
import time


class UrlConfig(db.Document):
    """
    url配置
    """
    name = db.StringField()
    prefix = db.StringField()
    host = db.StringField()
    api = db.StringField()
    create_at = db.IntField()


class Mark(db.Document):
    """
    mark
    """
    title = db.StringField(verbose_name='标题')
    method = db.StringField(verbose_name="方法")
    url = db.ReferenceField(UrlConfig, verbose_name='路由', reverse_delete_rule=2)
    path = db.StringField()
    input = db.StringField()
    output = db.StringField()
    create_at = db.IntField(default=int(time.time()))
