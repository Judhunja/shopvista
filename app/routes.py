""" This module contains signup and login routes """
from flask import (
    Flask, render_template, flash, redirect, url_for, session
)
from .models import db
from .forms import LoginForm, SignupForm
from .models import User, Product

app = Flask(__name__)


@app.route("/")
def home():
    """Home page"""
    products = Product.query.all()
    return render_template("home.html", products=products)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Route for logging in a user"""
    form = LoginForm()
    if form.validate_on_submit():
        # get first user in db
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.validate_password(form.password.data):
            flash(f"{form.username.data} logged in successfully!")
            return redirect(url_for("home"))
        elif (
                user is not None and
                not user.validate_password(form.password.data)
        ):
            flash("Invalid password")
        else:
            flash("Invalid username")
    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Route for signing up a user"""
    form = SignupForm()
    if form.validate_on_submit():
        # check for already existing username
        username_exists = User.query.filter_by(username=form.username.data)
        if username_exists is not None:
            flash("Username already taken")
            return render_template('signup.html', form=form)

        # check for already existing email
        email_exists = User.query.filter_by(email=form.email.data)
        if email_exists is not None:
            flash("Email already registered")
            return render_template('signup.html', form=form)

        # if email and username are new, create a new User
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Signed up successfully!")

        # redirect to login page for user to log in
        return redirect(url_for("login"))
    return render_template("signup.html", form=form)


@app.route('/product/<int:id>')
def product(id):
    """ Get more info about a product """
    product = Product.query.get_or_404(id)
    return render_template("product.html", product=product)


@app.route('/cart/<int:product_id>')
def cart(product_id):
    """ Add product user want to cart """
    cart = session.get('cart', [])
    cart.append(product_id)
    # store cart item as signed cookies
    session['cart'] = cart
    return redirect(url_for('see_cart'))


@app.route('/see_cart')
def see_cart():
    """ User view what is in their cart """
    cart = session.get('cart', [])
    if not cart:
        flash('You have no items in your cart')
    # view all items in cart
        return render_template('cart.html', products=[])

    products = Product.query.filter(Product.id.in_(cart)).all()

    return render_template('cart.html', products=products)
