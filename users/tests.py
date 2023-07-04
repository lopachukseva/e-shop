from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse("register")
        self.data = {
            "first_name": "Anonym",
            "last_name": "Anonym",
            "username": "anonym",
            "email": "anonym@anon.com",
            "password1": "Hbfh35282hdf",
            "password2": "Hbfh35282hdf",
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Регистрация")
        self.assertTemplateUsed(response, "users/register.html")

    def test_user_registration_post(self):
        username = self.data["username"]

        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("login"))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expire_at.date(),
            (now() + timedelta(hours=48)).date()
        )
