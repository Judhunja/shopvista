""" This module contains a class LoginForm """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


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
