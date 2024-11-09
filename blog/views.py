from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})