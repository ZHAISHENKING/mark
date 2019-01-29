#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from flask import request, make_response, render_template

from flask_restful import Resource
from utils.common import catch_exception
from .models import Mark, UrlConfig


class CreateMarkAPI(Resource):
    def __init__(self):
        a = UrlConfig.objects.all()
        self.url_list = [i["name"] for i in a]

    def get(self):
        return make_response(render_template('mark.html', url_list=self.url_list))

    @catch_exception
    def post(self):
        data = request.values
        url_config = data["url"]
        url = UrlConfig.objects.get(name=url_config)
        return_url = "%s://%s/%s" % (url["prefix"], url["host"], url["api"])
        mark = Mark(
            title=data["title"],
            url=url,
            func=data["func"],
            input=data["input"],
            path=data["path"],
            output=data["output"],
            err_output=data["err_output"],
            create_at=int(time.time())
        )
        mark.save()
        result = """
# {}
----

**{}**  `{}`

**参数**

```json
{}
```

**成功回调**

```json
{}
```

**失败回调**

```json
{}
```
"""

        result = result.format(data["title"], data["method"], return_url+data["path"], data["input"], data["output"], data["err_output"])
        return make_response(render_template("result.html", a=result, func=data["func"]))

