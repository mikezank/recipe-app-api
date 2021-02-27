from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        email = 'test@zsoft.io'
        password = 'testing123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@ZSOFT.IO'
        user = get_user_model().objects.create_user(email, 'junkpass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'junkpass')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@zsoft.io', 'junkpass')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
