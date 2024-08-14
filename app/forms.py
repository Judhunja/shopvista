""" This module contains a class LoginForm """
from flask import Flask
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
import secrets

app = Flask(__name__)
sec_key = secrets.token_urlsafe(16)
app.secret_key = sec_key

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


class LoginForm(FlaskForm):
    """ Form for logging in a user """
    email = StringField('Enter your email', validators=[
                        DataRequired(), Length(10, 40)])
    password = PasswordField('Enter your password', validators=[
        DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """ Form for signing up a new user """
    username = StringField('Enter your username', validators=[
                           DataRequired(), Length(10, 40)])
    email = StringField('Enter your email', validators=[
                        DataRequired(), Length(10, 40)])
    password = PasswordField('Enter your password', validators=[
        DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')
