from django.test import TestCase, Client
from faker import Faker
from .models import User

fake = Faker()


class UserModelTestCase(TestCase):
    """This test case will test the basics startuctural parts of our model"""

    def setUp(self):
        self.user = User()

    def test_model_has_basic_fields(self):
        """Checking only if name and mail are presents"""
        self.assertTrue(hasattr(self.user, 'name'))
        self.assertTrue(hasattr(self.user, 'mail'))

    def test_string_presentation_of_user_by_name(self):
        """Only check about presentation string format"""
        self.user.name = 'Ryan'
        self.assertEqual(self.user.__repr__(), '<User: Ryan>')


class AuthenticationTestCase(TestCase):
    """This test case is only responsible for realize the user authentication"""

    def setUp(self):
        self.user = User.objects.create(
            username='ryan',
            password='',
            name='Ryan Lessa',
            mail='ryancllessa@gmail.com'
        )
        # password hash
        self.user.set_password('embosa')
        self.user.save()
        # client
        self.client = Client()

    def test_check_authentication(self):
        """Check endpoint for authentication"""
        self.client.post('/authenticate', dict(
            username='ryan',
            password='embosa'
        ))

        result = self.client.get('/protected')
        self.assertEqual(result.status_code, 200)

        self.client.get('/logout')
        result = self.client.get('/protected')
        self.assertEqual(result.status_code, 302)
