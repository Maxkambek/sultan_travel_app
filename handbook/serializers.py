from .models import Handbook
from rest_framework import serializers


class HandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbook
        fields = ['id', 'name', 'description', 'some_text']


