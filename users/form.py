from .models import User
from wtforms import form, fields, validators
import flask_login as login


class LoginForm(form.Form):
    name = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('用户不存在')

        if user.password != self.password.data:
            raise validators.ValidationError('密码错误')

    def get_user(self):
        return User.objects.get(name=self.name.data)


class RegistrationForm(form.Form):
    name = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if User.objects(name=self.name.data):
            raise validators.ValidationError('用户名已注册')