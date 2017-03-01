from django.conf.urls import url
from posts import views


app_name = 'posts'

urlpatterns = [
    url(r'^create_post/', views.create_post, name='create_post'),
]