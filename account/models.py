from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.

def birthdate_validation(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date of birth cannot be in the future.')

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email = self.normalize_email(
                email
            )
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Admin(AbstractBaseUser):

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    firstname = models.CharField(verbose_name='First name', max_length=255, null=True, blank=True)
    lastname = models.CharField(verbose_name='Last name', max_length=255, null=True, blank=True)
    mobile_no = PhoneNumberField(help_text='(e.g +918457221548)', region="IN", null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )
    gender = models.CharField(verbose_name='Gender', choices=GENDER_CHOICE, null=True, blank=True, max_length=10)
    date_of_birth = models.DateField(validators=[birthdate_validation], null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["id", "email"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Faculty(Admin):
    class Meta:
        proxy = True