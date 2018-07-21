from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime


# Create your views here.

# in this pratice, i leave the elder code. But in real project, just delete the code when you don't need anymore
# def homepage(request):
#     posts = Post.objects.all()
#     posts_lists = list()
#     for count, post in enumerate(posts):
#         posts_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
#
#     return HttpResponse(posts_lists)

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())

    except:
        return redirect('/')