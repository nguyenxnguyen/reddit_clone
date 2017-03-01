from django.conf.urls import url
from home import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^(?P<pk>[0-9]+)/upvote/', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote/', views.downvote, name='downvote'),
]
