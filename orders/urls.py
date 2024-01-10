from django.urls import path
from . import views

urlpatterns = [
    path('order-create/', views.OrderCreateAPIView.as_view()),
    path('order-list/', views.OrderListAPIView.as_view()),
    path('confirm-order/<int:pk>/', views.ConfirmPaymentAPIView.as_view())
]
