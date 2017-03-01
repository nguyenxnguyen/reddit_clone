from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models


# Create your views here.
@login_required
def create_post(request):
    if request.method == "POST":
        info = request.POST
        if info['title_post'] and info['url_post']:
            post = models.Post()
            post.title = info['title_post']
            post.url = info['url_post']
            post.pub_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('home:index')
        else:
            msg = 'You must fill Title and URL'
            render(request, 'create_post.html', {'msg': msg})
    return render(request, 'create_post.html')
