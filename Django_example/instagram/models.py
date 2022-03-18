from django.db import models
import os
from uuid import uuid4
from django.utils import timezone

def uuid_name_upload_to(instance, filename):
        app_label = instance.__class__._meta.app_label
        cls_name = instance.__class__.__name__.lower()
        ymd_path = timezone.now().strftime('%Y/%m/%d')
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return '/'.join([
            app_label,
            cls_name,
            ymd_path,
            uuid_name[:2],
            uuid_name + extension,
        ])

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정시간')

    def __str__(self):
        #return f"Custom Post object ({self.id})"
        return self.message
    
    def message_length(self): 
        return len(self.message)
    message_length.short_description = '메세지 글자수'
 