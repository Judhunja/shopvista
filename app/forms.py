""" This module contains a class LoginForm """
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField, StringField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    """ Form for logging in a user """
    email = EmailField('Enter your email', validators=[
        DataRequired(), Email(), Length(6, 40)])
    password = PasswordField('Enter your password', validators=[
        DataRequired(), Length(7, 40)])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """ Form for signing up a new user """
    email = EmailField('Enter your email', validators=[
        DataRequired(), Email(), Length(6, 40)])
    username = StringField('Enter username', validators=[
                           DataRequired(), Length(2, 40)])
    password = PasswordField('Enter your password', validators=[
        DataRequired(), Length(7, 40)])
    confirm_password = PasswordField('Enter your password', validators=[
        DataRequired(), Length(7, 40)])
    submit = SubmitField('Submit')


class CheckoutForm(FlaskForm):
    """ Form for setting csrf for purchase(No field) """
    pass
