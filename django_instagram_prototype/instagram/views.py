import re
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404 # 템플릿 응답을 위한 shortcut 함수
from .models import Post
from django.views.generic import DetailView, ArchiveIndexView, ListView, YearArchiveView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import PostForm
from django.contrib import messages

@login_required
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # 현재 로그인 유저 Instance
            post.save()
            return redirect(post)
    else:
        form = PostForm()
        return render(request, 'instagram/post_form.html', {
        'form':form,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 작성자 check
    if post.author != request.user:
        messages.error(request, '작성자만 수정할 수 있습니다.')
        return redirect(post)

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=True) # DB에 모델 객체 저장
            return redirect(post)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'instagram/post_form.html', {
    'form':form,
    })

# @login_required
# def post_list(request:HttpRequest):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     page = request.GET.get('page', '1')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     paginator = Paginator(qs, 10) # 한 페이지당 10개씩
#     page_obj = paginator.get_page(page)
#     return render(request, 'instagram/post_list.html', {
#         'post_list':page_obj,
#         'q':q,
#     })#

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10
    
post_list = PostListView.as_view()

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

# def archives_year(request:HttpRequest, year) -> HttpResponse:
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)