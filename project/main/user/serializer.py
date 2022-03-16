from rest_framework import serializers
from .models import CustomUser, EmailValidation


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(style={"input_type": "password"},
                                     required=True, allow_blank=False, allow_null=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'name', 'phone_number', 'address','is_active']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'name', 'phone_number', 'address','is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EmailActivisionSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(required=True, allow_null=False)
    email = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    class Meta:
        model = EmailValidation
        fields = ['id', 'email','code']