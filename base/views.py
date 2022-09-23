from django.shortcuts import render
from .models import Post
# Create your views here.

def public_feed(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,'feed.html',context)
