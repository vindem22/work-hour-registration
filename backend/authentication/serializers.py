from rest_framework import serializers
from authentication.models import CoreUser
from api.models import Employee
from authentication.exceptions import CustomValidationError
from django.contrib.auth.password_validation import (
    validate_password,
    CommonPasswordValidator,
)
from django.core.exceptions import ValidationError
from authentication.helpers import get_or_none
from authentication.const_variables import *

class RegistrationDataValidationSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    email = serializers.EmailField(allow_blank=True)
    password = serializers.CharField(allow_blank=True)
    password_confirmation = serializers.CharField(allow_blank=True)


    def validate(self, attrs):
        errors = {}
        user_with_email = get_or_none(Employee, email=attrs.get('email'))
        if len(attrs.get('email')) == 0:
            errors['email'] = [SETTINGS_ERROR_ENTER_MAIL]
        if attrs.get('password') != attrs.get('password_confirmation'):
            errors['password_confirmation'] = [
                SETTINGS_ERROR_USER_PASSWORD_CONFIRMED
            ]
        try:
            validate_password(attrs.get('password'), CommonPasswordValidator)
        except ValidationError:
            errors['password'] = [LOGIN_WEAK_PASSWORD]
            if len(attrs.get('password')) < 7:
                errors['password'].append(
                    SETTINGS_ERROR_USER_PASSWORD_MIN
                )
        if user_with_email:
            errors['email'] = [SETTINGS_ERROR_USER_EMAIL_UNIQUE]
        if len(attrs.get('first_name')) == 0:
            errors['first_name'] = [SETTINGS_ERROR_ENTER_A_NAME]
        if len(attrs.get('last_name')) == 0:
            errors['last_name'] = [
                SETTINGS_ERROR_ENTER_YOUR_LAST_NAME
            ]
        if errors:
            raise CustomValidationError({'errors': errors}, 400)
        return attrs


class RegistrationSerializer(serializers.Serializer):
    def save(self, data):
        if not CoreUser.objects.filter(
        email=data.get('email')):
            CoreUser.objects.create_user(
                email=data.get('email'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
            )
        else:
            raise CustomValidationError(
                {'error': 'Email must be unique'}, 400
            )

class AuthUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'work_hours',
            'emp1__email',
            'emp2__email'
        )