from rest_framework import generics
from .serializers import PreparationSerializer
from .models import Preparation


class PreparationListAPIView(generics.ListAPIView):
    queryset = Preparation.objects.all()
    serializer_class = PreparationSerializer



