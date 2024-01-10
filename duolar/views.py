from .models import UmraDuo
from .serializers import UmraDuoSerializer
from rest_framework import generics


class UmraDuoListAPIView(generics.ListAPIView):
    queryset = UmraDuo.objects.all()
    serializer_class = UmraDuoSerializer
