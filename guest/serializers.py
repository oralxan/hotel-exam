from rest_framework.serializers import ModelSerializer
from .models import Guest

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = (          
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email',
            'passport_serie',
            'password'

            )