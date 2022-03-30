from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404 # 템플릿 응답을 위한 shortcut 함수
from .models import Post
from django.views.generic import DetailView

def post_list(request:HttpRequest):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list':qs,
        'q':q,
    })

def post_detail(requset:HttpRequest, pk) -> HttpResponse: 
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404
    if not requset.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk, is_public=True)
    else:
        post = get_object_or_404(Post, pk=pk)

    return render(requset, 'instagram/post_detail.html', {
        'post':post
    })
# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='pk')

def archives_year(request:HttpRequest, year) -> HttpResponse:
    return HttpResponse(f"{year}년 archives")