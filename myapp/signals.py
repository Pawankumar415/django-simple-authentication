from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models import LoginDetail
from django.contrib.auth.models import User  # Import the User model


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    LoginDetail.objects.create(
        user=user,
        username=user.username,  # Store the username in the LoginDetail model
        login_time=timezone.now(),
    )


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    login_detail = LoginDetail.objects.filter(user=user, logout_time__isnull=True).last()
    if login_detail:
        login_detail.logout_time = timezone.now()
        login_detail.save()
