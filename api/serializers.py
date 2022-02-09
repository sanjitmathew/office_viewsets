from rest_framework import serializers
from .models import Users, Teams


class TeamsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class UsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
