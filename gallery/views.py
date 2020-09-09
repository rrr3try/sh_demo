from rest_framework import generics

from gallery.models import Image
from gallery.serializers import ImageSerializer


class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get', 'post']


class ImageRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get', 'put', 'delete']
