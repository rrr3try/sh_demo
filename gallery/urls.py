from django.urls import path

from gallery.views import *

app_name = 'gallery'

urlpatterns = [
    path('', ImageListCreateView.as_view(), name='image'),
    path('<int:pk>', ImageRUDView.as_view(), name='image'),
    # comment
]
