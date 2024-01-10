from django.urls import path
from .views import PreparationListAPIView

urlpatterns = [
    path('', PreparationListAPIView.as_view())
]
