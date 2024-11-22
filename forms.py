from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    submit = SubmitField('Đăng nhập')

class ScheduleForm(FlaskForm):
    date = DateField('Ngày', validators=[DataRequired()])
    shift = StringField('Ca trực', validators=[DataRequired()])
    submit = SubmitField('Tạo lịch')
