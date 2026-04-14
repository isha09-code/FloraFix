from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},   # hide password in API responses
            'email': {'required': True},        # make email mandatory
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # remove password before creating user
        user = User(**validated_data)
        user.set_password(password)  # hash password properly
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)  # don't return raw password