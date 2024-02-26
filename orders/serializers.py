from .models import Order
from rest_framework import serializers
from main.serializers import TourSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_amount', 'order_date', 'tour', 'count_client', 'is_paid']


class OrderListSerializer(serializers.ModelSerializer):
    tour = TourSerializer(many=False)

    class Meta:
        model = Order
        fields = ['id', 'order_amount', 'order_date', 'tour', 'count_client', 'is_paid']


class ConfirmPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'is_paid']
