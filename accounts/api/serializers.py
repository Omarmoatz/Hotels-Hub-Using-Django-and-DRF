from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
        )

class UserDetailSerializer(serializers.ModelSerializer):
    code = serializers.CharField( read_only=True)
    verified = serializers.BooleanField( read_only=True)
    date_joined = serializers.DateTimeField( read_only=True)
    last_login = serializers.DateTimeField( read_only=True)
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",

            "gender",
            "phone",
            "address",
            "country",
            "image",
            "facebook",
            "twitter",

            "verified",
            "created",
            "modified",
            "date_joined",
            "last_login",
            "code",
        )

class UserCreateSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField( write_only=True)
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password_confirm",
        )