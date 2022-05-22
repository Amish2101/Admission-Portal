from wsgiref.validate import validator

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

from .models import Faculty

class FacultyRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    email = serializers.EmailField(validators=[UniqueValidator(
        Faculty.objects.all(),
        "Email already registered",
    ), ])
    password = serializers.CharField(
        required=True, validators=[validate_password])
    mobile_no = serializers.CharField(
        validators=[UniqueValidator(
            Faculty.objects.all(),
            "Mobile number already registered"
        )]
    )

    class Meta:
        model = Faculty
        fields = ('token', 'id', 'email', 'password', 'firstname',
                  'lastname', 'gender', 'date_of_birth', 'mobile_no')
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        data = super().create(validated_data)
        data.set_password(make_password(validated_data['password']))
        return data     

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
