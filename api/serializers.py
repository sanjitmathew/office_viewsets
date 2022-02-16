from rest_framework import serializers
from .models import Users, Teams


class TeamsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class UsersModelSerializer(serializers.ModelSerializer):

    def validate(self, attrs):

        if 'ph_no' in attrs.keys():
            if not attrs['ph_no'].isnumeric():
                raise serializers.ValidationError({'ph_no': 'phone no: should be of digits'})

            if len(attrs['ph_no']) < 10:
                raise serializers.ValidationError({'ph_no': 'phone no: less than 10 digits'})

        return attrs

    class Meta:
        model = Users
        fields = '__all__'
