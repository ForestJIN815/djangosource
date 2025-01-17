from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 모델에서 사용할 필드 지정
        # 방법 1
        # fields = "__all__"
        # exclude_fields = ["created_at", "modified_at"]
        # 방법 2
        fields = ["title", "content", "image", "tags"]
