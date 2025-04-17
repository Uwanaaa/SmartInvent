from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from django.shortcuts import get_object_or_404



class UserSerializer(ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def update(self, id, *args, **kwargs):
     try:
        user = get_object_or_404(User, id=id)

        for key, value in self.validated_data.items():
            if key == "username":
                if user.username != value:
                 if User.objects.exclude(id=user.id).filter(username=value).exists():
                    raise serializers.ValidationError({"username": "This username is already taken."})
                 setattr(user, key, value)

            elif key == "password":
                if value:  
                    user.set_password(value) 
            else:
                setattr(user, key, value)

        user.save()
        return user

     except Exception as e:
        print(f'Error: {e}')
        raise e
       



class CustomSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.CharField(required=False, allow_blank=True)
        self.fields['username'] = serializers.CharField(required=True, allow_blank=False)
        self.fields['password'] = serializers.CharField(required=True, allow_blank=False)

    def validate(self, attrs):
        username_field = attrs.get('username')
        password_field = attrs.get('password')

        try:
            user = User.objects.get(username=username_field)

        except User.DoesNotExist:
            raise AuthenticationFailed('This user does not exist')

        if not user.check_password(password_field):
            raise AuthenticationFailed('Incorrect password')

        token = RefreshToken.for_user(user) 

        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }
       
       
