from flask_wtf import FlaskForm
from wtforms import StringField,  TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력하세요.')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])

class UserCreateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', 'You put wrong password in check.')])
    password2 = PasswordField('Password Check', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])