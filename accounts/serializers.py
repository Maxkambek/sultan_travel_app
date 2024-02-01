from .models import Account, AccountDetails, VerifyPhone
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class VerifyPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = ['phone', 'code']


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ['id', 'user', 'full_name', 'passport_file']


class VerifyPhoneSerializer2(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=8)

    class Meta:
        model = VerifyPhone
        fields = ['phone', 'code', 'password']
