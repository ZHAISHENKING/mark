from flask import request, session, current_app
from flask_restful import Resource
from .models import *
from .code import verify, Code
from utils.common import *
from utils.auth import Auth
from flask import render_template, make_response
from .form import LoginForm, RegistrationForm, login


class Register(Resource):
    """用户注册"""
    def __init__(self):
        self.form = RegistrationForm(request.form)

    def get(self):
        code = Code().get()
        return make_response(render_template("reg.html", code=code))

    @catch_exception
    def post(self):
        data = request.values

        if data["username"]:
            if User.objects.filter(username=data["username"]).first():
                return falseReturn("用户已存在")
            else:
                if verify(data):
                    user = User(
                        username=data["username"],
                        password=data["password"]
                    )
                    user.save()
                    if user.id:
                        return Auth.authenticate(Auth, data["username"], data["password"])
                    else:
                        return falseReturn("注册失败")
                else:
                    return falseReturn("验证码错误")
        else:
            return falseReturn("请输入用户名")


class Login(Resource):
    """用户登录"""
    def __init__(self):
        self.form = LoginForm(request.form)

    def get(self):
        return make_response(render_template('login.html'))

    @catch_exception
    def post(self):
        data = request.values
        print(data["username"])
        username = data["username"]
        password = data["password"]
        if not username or not password:
            return falseReturn("用户名和密码不能为空")
        else:
            return Auth.authenticate(Auth, username, password)