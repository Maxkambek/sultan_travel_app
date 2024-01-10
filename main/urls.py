from .views import NewsListAPIView, ToursListAPIView, TourDetailAPIView
from django.urls import path

urlpatterns = [
    path('', NewsListAPIView.as_view()),
    path('tours/', ToursListAPIView.as_view()),
    path('tours/<int:pk>/', TourDetailAPIView.as_view())
]
