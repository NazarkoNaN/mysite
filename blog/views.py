from django.shortcuts import render
from django.utils import timezone
from .models import Post
def startpage(request):
    return render(request, 'blog/start-page.html')

def post_list(request):
    posts = Post.objects.filter().order_by('creted_date')
    return render(request, 'blog/post_list.html', {'posts': posts})