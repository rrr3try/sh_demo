from django.urls import path

from gallery.views import ImageListCreateView

app_name = 'gallery'

urlpatterns = [
    path('', ImageListCreateView.as_view(), name='image')
    # comment
]
