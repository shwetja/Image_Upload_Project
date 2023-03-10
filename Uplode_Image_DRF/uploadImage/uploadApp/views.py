from rest_framework import viewsets
from .serializers import ImageSerializer
from .models import Image


class ImageModelViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
