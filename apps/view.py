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
        "prefix", "host", "api"
    )

    def __init__(self, **kwargs):
        super(URLView, self).__init__(UrlConfig, **kwargs)