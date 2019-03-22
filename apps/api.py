#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from flask import request, make_response, render_template, url_for, redirect
from utils.constant import FIELD_CHOICE
from flask_restful import Resource
from utils.common import catch_exception, error_return, trueReturn
from .models import Mark, UrlConfig, Field, Table, DIYApp
from .serializers import SubmitTableSchema, DIYAppSchema, TableSchema


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


class Nav(Resource):
    def get(self):
        return make_response(render_template('nav.html'))


class AppApi(Resource):
    def get(self):
        name = request.args["name"]
        app = DIYApp.objects(name=name).first()
        result = DIYAppSchema().dump(app).data
        return make_response(render_template("apps.html", fields=FIELD_CHOICE, app=result))


class SubmitTable(Resource):
    """
    提交表格,类型为单个对象
    example:
    {
        "table_name": "aa",
        "verbose_name": "bb",
        "field": []
    }
    """
    @catch_exception
    def post(self):
        data = request.json
        schema = SubmitTableSchema()
        errors = schema.validate(data)
        if errors:
            return error_return(10000, str(errors), "")

        table = schema.load(data)
        table = table.data

        table.save()

        for i in data["field"]:
            field = Field(**i)
            field.save()
            table.fields.append(field)
        table.save()
        result = TableSchema().dump(table).data
        return trueReturn(result)


class SubmitApp(Resource):
    """
    更新app
    :param: str app_id
    :param: list table_list
    {
        "app_id": "xx",
        "table_list": ["xx", "xx"]
    }
    """
    @catch_exception
    def post(self):
        data = request.json
        schema = DIYAppSchema()
        errors = schema.validate(data)
        if errors:
            return error_return(10000, str(errors), "")
        table_list = Table.objects.filter(pk__in=data["table_list"])
        app = DIYApp.objects.with_id(data["app_id"])
        app.update(table_list=table_list)
        app.reload()
        result = schema.dump(app).data
        return trueReturn(result)


class CreateApp(Resource):
    """
    创建app
    :param: name
    """
    @catch_exception
    def post(self):
        data = request.values
        schema = DIYAppSchema()
        diy = schema.load(data).data
        diy.save()
        return redirect(url_for('index.app', name=diy.name))


class GetApp(Resource):
    """获取app"""
    def get(self):
        data = request.args
        diy = DIYApp.objects.with_id(data["id"])
        schema = DIYAppSchema()
        info = schema.dump(diy).data
        return trueReturn(info)