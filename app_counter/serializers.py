from django.contrib.auth.models import User
from rest_framework import serializers
from app_counter.models import Counter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CounterSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Counter
        fields = ['id', 'value', 'user']
