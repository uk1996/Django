from django.db import models
import os
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.core.validators import MinLengthValidator

def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label # 앱 별로
    cls_name = instance.__class__.__name__.lower() # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d') # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출
    return '/'.join([
        app_label,
        cls_name,
        ymd_path,
        uuid_name + extension,
    ])


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
    related_name='instagram_post_set') # reverse_name을 포기하려면 related_name='+'
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    message = models.TextField(validators=[MinLengthValidator(10)])
    tag_set = models.ManyToManyField('Tag', blank=True) # ManyToManyField(to, blank)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateField(auto_now=True) # 수정시간

    class Meta:
        ordering  = ['-id']

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

class Comment(models.Model):
    # models.ForeignKey 주석
    # to는 문자열로도 지정 가능 ex> 'instagram.Post'
    # on_delete: Record 삭제 시 Rule
    # on_delete=models.CASCADE: FK로 참조하하는 다른 모델의 Record들도 삭제 ex> 하나의 Post가 삭제되면 거기에 속하는 모든 Comment삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE, # post_id 필드가 생성(id는 Post Model의 pk), post는 가상의 필드
                                    limit_choices_to={'is_public':True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.name  