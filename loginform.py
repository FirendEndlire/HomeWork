from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username_spaceman = StringField('id астронафта', validators=[DataRequired()])
    password_spaceman = PasswordField('Пароль астронафта', validators=[DataRequired()])
    
    username_captain = StringField('id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    
    submit = SubmitField('Доступ')
    
