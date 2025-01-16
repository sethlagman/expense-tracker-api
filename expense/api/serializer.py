from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ExpenseSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Expense
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('User not found')
        
        return {'user': user}
