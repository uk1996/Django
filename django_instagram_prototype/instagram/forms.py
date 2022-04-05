from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['photo', 'message', 'tag_set', 'is_public'] # 지정된 필드에 한해서만 유효성 검사를 시행
        # exclude = []