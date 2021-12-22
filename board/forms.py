from django.contrib.auth.hashers import check_password

from django import forms
from .models import Board

class BoardForm(forms.Form):
    # 입력받을 값 두개
    title = forms.CharField(error_messages={
        'required': '제목을 입력하세요.'
    }, max_length=100, label="게시글 제목")
    contents = forms.CharField(error_messages={
        'required': '내용을 입력하세요.'
    }, widget=forms.Textarea, label="게시글 내용")