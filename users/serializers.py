from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'This email has already been selected'
            )
        return value

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('The email is not exists')
        return value
