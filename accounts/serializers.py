from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'shopname']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        user.save()
        return user
