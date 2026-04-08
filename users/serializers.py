from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import ConfirmationCode

User = get_user_model()

class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('User already exists!')


class ConfirmUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        username = data['username']
        code = data['code']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден")

        try:
            confirmation = ConfirmationCode.objects.get(user=user)
        except ConfirmationCode.DoesNotExist:
            raise serializers.ValidationError("Код подтверждения не найден")

        if confirmation.code != code:
            raise serializers.ValidationError("Неверный код")

        data['user'] = user
        return data

    def save(self, **kwargs):
        user = self.validated_data['user']
        user.is_active = True
        user.save()
        user.confirmation_code.delete()  
        return user