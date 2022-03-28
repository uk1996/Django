from django.http import HttpRequest, HttpResponse
from django.shortcuts import render # 템플릿 응답을 위한 shortcut 함수
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list':qs,
        'q':q,
    })

def post_detail(requset, pk):
    pass