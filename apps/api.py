#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import bson.binary
import bson.objectid
import bson.errors
import time
from flask import request, make_response, render_template
from bson.objectid import ObjectId
from flask import redirect, current_app, Response, send_from_directory
from flask_restful import Resource
from utils.common import trueReturn, falseReturn, ms, catch_exception
from .models import Mark, UrlConfig
from mongoengine.queryset.visitor import Q
import html


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
        print(return_url)
        # mark = Mark(
        #     title=data["title"],
        #     url=url,
        #     input=data["input"],
        #     path=data["path"],
        #     output=data["output"],
        #     create_at=int(time.time())
        # )
        # mark.save()
        result = """
        <pre>
# {}
----

`{}` **{}**

输入

```json
{}
```

输出

```json
{}
```
</pre>

"""

        result = result.format(data["title"], data["method"], return_url+data["path"], data["input"], data["output"])
        return make_response(render_template("result.html", a=result))

