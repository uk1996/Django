from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(requset):
    qs = Post.objects.all()
    return render(requset, 'blog1/post_list.html', {
        'post_list':qs,
    })