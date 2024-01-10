from .models import Handbook
from .serializers import HandbookSerializer
from rest_framework import generics


class HandbookListAPIView(generics.ListAPIView):
    queryset = Handbook.objects.all()
    serializer_class = HandbookSerializer
