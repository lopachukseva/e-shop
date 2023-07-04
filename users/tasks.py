import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailVerification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expire_at = now() + timedelta(hours=48)
    code = uuid.uuid4()
    record = EmailVerification.objects.create(code=code, user=user, expire_at=expire_at)
    record.send_verification_email()
