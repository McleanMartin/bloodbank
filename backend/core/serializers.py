from rest_framework import serializers
from core.models import *


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ['email',
                'national_ID',
                'phone_number',
                'date_of_birth',
                'password',
                ]
    

    def create(self, validated_data):
        email = validated_data.get('email')
        national_ID= validated_data.get('national_ID')
        phone_number = validated_data.get('phone_number')
        date_of_birth = validated_data.get('date_of_birth')
        password = validated_data.get('password')
        user = CustomUser(email=email,
                        phone_number=phone_number,
                        national_ID=national_ID,
                        date_of_birth=date_of_birth,
                        )

        user.set_password(password)
        user.is_admin = False
        user.save()
        return  user