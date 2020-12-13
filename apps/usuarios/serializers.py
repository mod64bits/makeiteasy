from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', 'email',  'password',  'is_staff', 'is_active']
        error_message='Credenciais Invalidas'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],

        )

        user.set_password(validated_data['password'])
        user.save()
        return user


