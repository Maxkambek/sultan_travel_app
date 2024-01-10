from .models import Order
from .serializers import OrderSerializer, OrderListSerializer, ConfirmPaymentSerializer
from rest_framework import generics, authentication, permissions


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset


class ConfirmPaymentAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = ConfirmPaymentSerializer
