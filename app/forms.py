# 创建一个登录表单，用户用于认证系统。
# 在我们应用程序中支持的登录机制不是标准的用户名/密码类型，
# 我们将使用 OpenID。OpenIDs 的好处就是认证是由 OpenID 的提供者完成的，
# 因此我们不需要验证密码，这会让我们的网站对用户而言更加安全。
#
# OpenID 登录仅仅需要一个字符串，被称为 OpenID。
# 我们将在表单上提供一个 ‘remember me’ 的选择框，
# 以至于用户可以选择在他们的网页浏览器上种植 cookie ，
# 当他们再次访问的时候，浏览器能够记住他们的登录
#
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)

# add edit form
class EditForm(Form):
    nickname = StringField('nickname', validators= [DataRequired()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max =140)])

    # add validation
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
