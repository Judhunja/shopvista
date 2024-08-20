""" This module contains signup and login routes """
from flask import (
    render_template, flash, redirect, url_for, session, request
)
from .models import db
from .forms import LoginForm, SignupForm
from .models import User, Commodity


def register_routes(app):
    @app.route("/")
    def home():
        """Home page"""
        product_searched = request.args.get('search')
        category_selected = request.args.get('category')

        products_query = Commodity.query

        if product_searched:
            products_query = products_query.filter(
                Commodity.name.ilike(f'%{product_searched}%'))

        if category_selected:
            products_query = products_query.filter(
                Commodity.category == category_selected)

        products = products_query.all()

        categories = db.session.query(Commodity.category).distinct().all()
        # get the category from the tuple
        categories = [c[0] for c in categories]
        return render_template("home.html",
                               products=products,
                               categories=categories,
                               category_selected=category_selected)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        """Route for logging in a user"""
        form = LoginForm()
        if form.validate_on_submit():
            # get first user in db
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.validate_password(form.password.data):
                session['user_id'] = user.id
                flash(f"{form.email.data} logged in successfully!")
                return redirect(url_for("home"))
            elif (
                user is not None and
                not user.validate_password(form.password.data)
            ):
                flash("Invalid password!")
            else:
                flash("Invalid email!")
        return render_template("login.html", form=form)

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        """Route for signing up a user"""
        form = SignupForm()
        if form.validate_on_submit():
            # check for already existing username
            username_exists = User.query.filter_by(
                username=form.email.data).first()
            if username_exists is not None:
                flash("Username already taken")
                return render_template('signup.html', form=form)

            # check for already existing email
            email_exists = User.query.filter_by(email=form.email.data).first()
            if email_exists is not None:
                flash("Email already registered!")
                return render_template('signup.html', form=form)

            # confirm user password
            if form.password.data != form.confirm_password.data:
                flash("Passwords do not match! Enter correct password")
                return render_template('signup.html', form=form)
            # if email and username are new, create a new User
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Signed up successfully!")

            # automatically login the user after signup
            return redirect(url_for("home"))
        return render_template("signup.html", form=form)

    @app.route('/product/<int:id>')
    def product(id):
        """ Get more info about a product """
        product = Commodity.query.get_or_404(id)
        # check if user is logged in
        user_id = session.get('user_id')
        return render_template("product.html", product=product, user_id=user_id)

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

        products = Commodity.query.filter(Commodity.id.in_(cart)).all()

        return render_template('cart.html', products=products)

    @app.route("/logout")
    def logout():
        """Route for logging out a user"""
        session.pop('user_id', None)
        flash("You have logged out!")
        return redirect(url_for("home"))
