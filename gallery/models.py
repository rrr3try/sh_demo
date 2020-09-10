from django.db import models


class Image(models.Model):
    name = models.TextField()
    image = models.ImageField()
    time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)



