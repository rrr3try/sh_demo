from django.urls import path

from gallery.views import *

app_name = 'gallery'


urlpatterns = [
    path('', ImageListCreateView.as_view(), name='image'),
    path('<int:pk>', ImageRUDView.as_view(), name='image-rud'),
    path('comment/', CommentCreateView.as_view(), name='comment'),
    path('<int:image>/comment/', CommentList.as_view(), name='comment-list'),
    path('<int:image>/comment/<int:comment>', CommentRUD.as_view(), name='comment-rud'),

]
