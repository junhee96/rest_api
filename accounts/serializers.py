from rest_framework import serializers
from .models import User
from django.core.validators import ValidationError
from django.contrib.auth import authenticate


class SignUpSerializer(serializers.ModelSerializer):
    '''
    회원가입 serializer
    '''
    class Meta:
        model = User
        fields = ("id", "username", "password", "nickname", "phone", "address", "gender")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        nickname = validated_data['nickname']
        phone = validated_data['phone']
        address = validated_data['address']
        gender = validated_data['gender']

        user = User(
            username = username,
            nickname = nickname,
            phone = phone,
            address = address,
            gender = gender,
        )
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    '''
    로그인 serializer
    '''
    username = serializers.EmailField()
    password = serializers.CharField()
   
    class Meta:
        model = User
        fields = ('password', 'username')
        extra_kwargs = {'password':{"write_only":True}}

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("가입된 고객이 아닙니다.")
    
class ProfileSerializer(serializers.ModelSerializer):
    '''
    정보조회 serializer
    '''
    class Meta:
        model = User
        fields = ("id", "username", "nickname", "phone", "address", "gender")
 
