from rest_framework.serializers import ModelSerializer

from gallery.models import Image, Comment


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
