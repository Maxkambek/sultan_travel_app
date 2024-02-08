from .serializers import NewsSerializer, TourSerializer, PhoneSerializer
from .models import News, Tour, Phone
from rest_framework import generics


class PhoneList(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ToursListAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourDetailAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
