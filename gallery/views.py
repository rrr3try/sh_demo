from rest_framework import generics
from rest_framework.generics import get_object_or_404

from gallery.models import Image, Comment
from gallery.serializers import ImageSerializer, CommentSerializer


class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get', 'post']


class ImageRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get', 'put', 'delete']


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'image'

    def get_queryset(self):
        image_id = self.kwargs['image']
        return Image.objects.get(pk=image_id).comments


class CommentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'image'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(
            queryset, **filter_kwargs,
            image__pk=self.kwargs['image'],
            pk=self.kwargs['comment']
        )

        self.check_object_permissions(self.request, obj)

        return obj
