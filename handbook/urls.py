from django.urls import path
from .views import HandbookListAPIView

urlpatterns = [
    path('', HandbookListAPIView.as_view())
]
