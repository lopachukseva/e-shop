from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()

    def __str__(self):
        return f"EmailVerification for {self.user.email}"

    def send_verification_email(self):
        link = reverse("email_verification", args=(self.user.email, self.code,))
        verification_link = f"{settings.DOMAIN_NAME}{link}"

        title = f"Подтверждение аккаунта для {self.user.username}"
        message = f"Для подтверждения аккаунта перейдите по ссылке: {verification_link}"
        send_mail(
            subject=title,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expire_at else False
