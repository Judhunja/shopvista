#!/usr/bin/python3
""" This module contains tests for shopvista routes """
import pytest
from flask import url_for
from flask_testing import TestCase
from app import create_app, db
from app.models import User, Commodity, Orders


class TestBase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://shopper:shopvistashopper@localhost/shopvista'
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        db.create_all()
        self.user = User(username='exampleuser', email='user@example.com')
        self.user.set_password('password')
        db.session.add(self.user)
        self.commodity = Commodity(
            name='Test Product', category='Electronics', price=100.00)
        db.session.add(self.commodity)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRoutes(TestBase):
    """ Contains all the tests for the routes """

    def test_home(self):
        """ Pull home page """
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertTemplateUsed('home.html')

    def test_login_success(self):
        """ Correct user login test """
        response = self.client.post(url_for('login'), data={
            'email': 'user@example.com',
            'password': 'password'
        })
        self.assertRedirects(response, url_for('home'))
        with self.client.session_transaction() as sess:
            assert sess['user_id'] == self.user.id

    def test_login_failure(self):
        """ Wrong user password test """
        response = self.client.post(url_for('login'), data={
            'email': 'user@example.com',
            'password': 'wrongpassword'
        })
        self.assert200(response)
        self.assertIn(b'Invalid password!', response.data)

    def test_signup_success(self):
        """ New correct signup """
        response = self.client.post(url_for('signup'), data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'confirm_password': 'newpassword'
        })
        self.assertRedirects(response, url_for('home'))
        user = User.query.filter_by(email='newuser@example.com').first()
        self.assertIsNotNone(user)

    def test_signup_failure_existing_email(self):
        """ Use already existing email """
        response = self.client.post(url_for('signup'), data={
            'username': 'newuser',
            'email': 'user@example.com',
            'password': 'password',
            'confirm_password': 'password'
        })
        self.assert200(response)
        self.assertIn(b'Email already registered!', response.data)

    def test_add_to_cart(self):
        """ Test add item to cart """
        response = self.client.get(
            url_for('cart', product_id=self.commodity.id))
        self.assertRedirects(response, url_for(
            'product', id=self.commodity.id))
        with self.client.session_transaction() as sess:
            cart = sess.get('cart', [])
            assert self.commodity.id in cart

    def test_remove_from_cart(self):
        """ Test remove commodity from cart """
        with self.client.session_transaction() as sess:
            sess['cart'] = [self.commodity.id]
        response = self.client.post(
            url_for('remove_from_cart', product_id=self.commodity.id))
        self.assertRedirects(response, url_for('see_cart'))
        with self.client.session_transaction() as sess:
            cart = sess.get('cart', [])
            assert self.commodity.id not in cart

    def test_view_cart(self):
        """ Test viewing cart """
        with self.client.session_transaction() as sess:
            sess['cart'] = [self.commodity.id]
        response = self.client.get(url_for('see_cart'))
        self.assert200(response)
        self.assertIn(b'Test Product', response.data)

    def test_checkout(self):
        """ Test congrats html template used in checkout """
        with self.client.session_transaction() as sess:
            sess['user_id'] = self.user.id
            sess['cart'] = [self.commodity.id]
        self.assertTemplateUsed('congrats.html')
        order = Orders.query.filter_by(user_id=self.user.id).first()
        self.assertIsNotNone(order)

    def test_logout(self):
        """ Test logout functionality """
        with self.client.session_transaction() as sess:
            sess['user_id'] = self.user.id
        response = self.client.get(url_for('logout'))
        self.assertRedirects(response, url_for('home'))
        with self.client.session_transaction() as sess:
            assert 'user_id' not in sess


if __name__ == '__main__':
    pytest.main()
