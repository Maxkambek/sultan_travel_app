from rest_framework import serializers
from .models import UmraDuo


class UmraDuoSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = UmraDuo
        fields = ['id', 'name', 'audio', 'description']
    
    def get_description(self, instance):
        from django.utils.safestring import mark_safe
        return mark_safe(instance.description)
