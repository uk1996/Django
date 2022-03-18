from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정시간')

    def __str__(self):
        #return f"Custom Post object ({self.id})"
        return self.message
    
    def message_length(self): 
        return len(self.message)
    message_length.short_description = '메시지 글자수'
