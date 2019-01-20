from .models import Mark, UrlConfig
from admin import ModelView


class MarkView(ModelView):
    """
    自定义视图
    """
    column_list = (
        "title", "method", "path"
    )

    def __init__(self, **kwargs):
        super(MarkView, self).__init__(Mark, **kwargs)


class URLView(ModelView):
    """
    自定义视图
    """
    column_list = (
       "name", "prefix", "host", "api"
    )

    column_labels = {
        "name": "接口名称",
        "prefix": "协议",
        "host": "域名",
        "api": "路径"
    }

    def __init__(self, **kwargs):
        super(URLView, self).__init__(UrlConfig, **kwargs)