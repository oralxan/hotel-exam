from rest_framework import serializers
from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Guest(
            username=validated_data['username'],
            email=validated_data['email'],
            fullname =validated_data['fullname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user