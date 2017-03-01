from django.shortcuts import render, redirect
from posts.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.order_by('votes_total')
    return render(request, 'index.html', {'posts': posts})


def upvote(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home:index')


def downvote(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home:index')

