from flask import Blueprint
from flask_restful import Api
from admin import Index, LogoutView, LoginView
from apps.api import CreateMarkAPI
from users.api import Register, Login


# 注册蓝图,路由前缀为/docs
uploadApi = Blueprint('api', __name__, url_prefix='/api')
viewApi = Blueprint('index', __name__, url_prefix='')
docs = Api(uploadApi)
view = Api(viewApi)

docs.add_resource(Index, '/', endpoint="index")                                                 # 后台主页
docs.add_resource(LoginView, '/login/', endpoint="login")                                       # 后台登录页
docs.add_resource(LogoutView, '/logout/', endpoint="logout")                                    # 后台退出登录
view.add_resource(CreateMarkAPI, '/mark', endpoint="mark")
view.add_resource(Register, '/reg', endpoint="reg")
