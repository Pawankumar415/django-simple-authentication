from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message='Phone number must be 10 digits and must be starts with 6 to 9'
)


class CustomUser(AbstractUser):
    phone = models.CharField(unique=True,
        max_length=10,
        validators=[phone_number_validator],
        help_text='Enter a 10-digit phone number.')
    address = models.CharField(max_length=100, blank=True)


class LoginDetail(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    username = models.CharField(max_length=150)  # Assuming unique usernames
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.login_time}"
