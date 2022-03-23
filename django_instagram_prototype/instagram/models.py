from django.db import models
import os
from django.utils import timezone
from uuid import uuid4

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
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering  = ['-id']

    def __str__(self):
        return self.message 
