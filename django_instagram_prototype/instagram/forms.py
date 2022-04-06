from django import forms
from flask import message_flashed
from .models import Post
import re

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['photo', 'message', 'tag_set', 'is_public'] # 지정된 필드에 한해서만 유효성 검사를 시행
        # exclude = []

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '영어가 한번이상 반복 되었습니다.', message)
        return message
