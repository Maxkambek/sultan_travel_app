from .models import Preparation
from rest_framework import serializers


class PreparationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preparation
        fields = ['id', 'text']
