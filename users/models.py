import time
from admin import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    """用户"""
    genderChoice = ((0, '女'),
                    (1, '男'))
    uid = db.SequenceField()
    username = db.StringField(max_length=30, verbose_name="姓名")
    password = db.StringField(verbose_name="密码")
    phone = db.StringField(verbose_name="手机号")
    email = db.EmailField(verbose_name="邮箱")
    year = db.StringField(verbose_name="出生年份")
    gender = db.IntField(verbose_name="性别", help="不填写，默认为女", default=0)
    create_date = db.DateTimeField(verbose_name="添加时间", default=datetime.now)
    login_time = db.IntField(default=int(time.time()))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def save(self, *args, **kwargs):
        if self.password:
            self.password = generate_password_hash(self.password)
            super(User, self).save(*args, **kwargs)
        else:
            super(User, self).save(*args, **kwargs)

    @staticmethod
    def set(password):
        return generate_password_hash(password)

    @staticmethod
    def check(hash, password):
        return check_password_hash(hash, password)

    def __unicode__(self):
        return self.username

    def __str__(self):
        return '%s' % self.username

    def get_id(self):
        return str(self.id)