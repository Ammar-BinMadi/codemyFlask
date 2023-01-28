from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user

# create Flask instance
app = Flask(__name__)
# add database
'''
Filters could be find at :    https://jinja.palletsprojects.com/en/3.1.x/templates/
some of them :
safe
capitalized
lower
upper
title
trim
striptags
'''


@app.route('/')
@app.route('/home')
def index():
    first_name = "ammar"
    stuff = "this is bold text"
    pizza = ["mozarila", "dynamite", "truffel", 44]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           pizza=pizza)


# localhost:5000/user/ammar
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",name=name)


# Create custom erorr pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
