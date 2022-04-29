# Generated by Django 3.2.13 on 2022-04-28 11:34

import account.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(help_text='(e.g +918457221548)', max_length=128, region='IN')),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='email address')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True, verbose_name='Gender')),
                ('date_of_birth', models.DateField(null=True, validators=[account.models.birthdate_validation])),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id', 'email'],
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.admin',),
        ),
    ]