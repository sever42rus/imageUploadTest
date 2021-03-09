from rest_framework import generics
from .models import Image
from .serializers import (
    ImageSerializer,
    ImageCreateSerializer
)

# Create your views here.


class ImageListAPI(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageCreateAPI(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer
