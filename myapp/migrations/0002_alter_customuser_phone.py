# Generated by Django 5.0 on 2023-12-18 12:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(help_text='Enter a 10-digit phone number.', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^[6-9]\\d{9}$')]),
        ),
    ]
