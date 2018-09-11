import unittest
import re
from app import create_app, db
from app.models import User, Role


class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('Friend' in response.get_data(as_text=True))

    def test_login(self):
        # register a new account
        response = self.client.post('/auth/register', data={
            'email': '401316161@qq.com',
            'username': 'john',
            'password': '123',
            'password2': '123'
        })
        self.assertTrue(response.status_code == 200)
        # login the account
        response = self.client.post('/auth/login',
                                    data={'email': '401316161@qq.com',
                                          'password': '123'}, follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('Profile' in data)
        # logout the account
        response = self.client.get('/auth/logout', follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('You have been logged out' in data)

    def test_post(self):
        response = self.client.post('/auth/login',
                                    data={'email': '401316161@qq.com',
                                          'password': '123'}, follow_redirects=True)

        user = User.query.filter_by(email='401316161@qq.com').first()
        token = user.generate_confirmation_token()

        response = self.client.get(
            '/auth/confirm/{}'.format(token), follow_redirects=True)

        user.confirm(token)

        data = response.get_data(as_text=True)

        # token

        self.assertTrue('You have confirmed your account' in data)

        response = self.client.post(
            '/', data={'body': 'body123'}, follow_redirects=True)
        data = response.get_data(as_text=True)

        self.assertTrue('body123' in data)
