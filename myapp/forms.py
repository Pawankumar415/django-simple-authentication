from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
User = get_user_model()

phone_number_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message='Phone number must be 10 digits and must be starts with 6 to 9'
)


class UserRegister(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(validators=[phone_number_validator])
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'phone', 'address', 'password1', 'password2']
