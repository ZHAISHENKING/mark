from admin import db
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
    url = db.ReferenceField(UrlConfig, verbose_name='路由', reverse_delete_rule=2)
    path = db.StringField()
    input = db.StringField()
    output = db.StringField()
    err_output = db.StringField()
    create_at = db.IntField(default=int(time.time()))
