from django.urls import path
from .views import UmraDuoListAPIView

urlpatterns = [
    path('', UmraDuoListAPIView.as_view())
]
