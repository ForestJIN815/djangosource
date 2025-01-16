from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    # email 은 필수 입력 요소는 아님 => 필수 입력 요소로 만들고 싶다면
    email = forms.EmailField(label="이메일", help_text="사용중인 이메일을 입력하세요")

    class Meta:
        model = User
        # fields = "__all__"
        # 회원가입할 때 사용하는 필드는 아이디,비밀번호,이메일이라고 할때
        # password 필드는 default 로 포함되기 때문에 나머지 필드만 작성
        fields = ["username", "email"]
