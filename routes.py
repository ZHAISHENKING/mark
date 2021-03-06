from flask import Blueprint
from flask_restful import Api
from admin import Index, LogoutView, LoginView
from apps.api import CreateMarkAPI, Nav, AppApi, CreateApp, SubmitTable, SubmitApp, GetApp
from users.api import Register, Login


# 注册蓝图,路由前缀为/docs
uploadApi = Blueprint('api', __name__, url_prefix='/api')
viewApi = Blueprint('index', __name__, url_prefix='')
docs = Api(uploadApi)
view = Api(viewApi)

docs.add_resource(Index, '/', endpoint="index")                                                 # 后台主页
docs.add_resource(LoginView, '/login/', endpoint="login")                                       # 后台登录页
docs.add_resource(LogoutView, '/logout/', endpoint="logout")                                    # 后台退出登录
view.add_resource(GetApp, '/get/app', endpoint="get_app")
view.add_resource(CreateMarkAPI, '/mark', endpoint="mark")
view.add_resource(Register, '/reg', endpoint="reg")
view.add_resource(Login, '/login', endpoint="login")
view.add_resource(Nav, '/nav', endpoint="nav")
view.add_resource(AppApi, '/app', endpoint="app")
docs.add_resource(CreateApp, '/create/app', endpoint="create_app")
docs.add_resource(SubmitTable, '/create/table', endpoint="add_table")
docs.add_resource(SubmitApp, '/update/app', endpoint="update_app")