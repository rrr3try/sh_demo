from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from gallery.models import Image
from gallery.serializers import ImageSerializer

client = Client()


class GetImagesTest(TestCase):
    """ Test module for images API """

    def setUp(self):
        self.image0 = Image.objects.create(name='image 0', image=ContentFile(b'stub'))
        self.image1 = Image.objects.create(name='image 1', image=ContentFile(b'stub'))
        self.image2 = Image.objects.create(name='image 2', image=ContentFile(b'stub'))

    def test_get_all_images(self):
        response = client.get(reverse('gallery:image'))
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_image(self):
        image_id = 1
        response = client.get(reverse('gallery:image-rud', kwargs={'pk': image_id}))
        image = Image.objects.get(pk=image_id)
        serializer = ImageSerializer(image)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        image_id = 1
        old_image = Image.objects.get(pk=image_id)
        response = client.patch(reverse('gallery:image-rud', kwargs={'pk': image_id}),
                                data={'name': 'image renamed'}, content_type='application/json')
        new_image = Image.objects.get(pk=image_id)
        serialized_new = ImageSerializer(new_image)
        serialized_old = ImageSerializer(old_image)
        self.assertNotEqual(response.data, serialized_old.data)
        self.assertEqual(response.data, serialized_new.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid(self):
        image_id = 5
        response = client.patch(reverse('gallery:image-rud', kwargs={'pk': image_id}),
                                data={'name': 'image renamed'}, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = client.get(reverse('gallery:image'))
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        image_id = 1
        response = client.delete(reverse('gallery:image-rud', kwargs={'pk': image_id}),)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            Image.objects.get(pk=image_id)
        except Exception as e:
            self.assertEqual(Image.DoesNotExist, type(e))
