from django import forms
from .models import Musician

# 장고의 폼 기능
# 폼 생성에 필요한 데이터를 폼 클래스로 구조화
# 폼 클래스의 데이터를 렌더링하여 HTML 폼 생성
# 사용자로부터 제출된 폼과 데이터를 수신하고 처리
# form : HTML 의 <form> or form 을 만들어내는 Form 클래스 or 서버로 전송된 구조화된 데이터


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"
        # fields = ["name"]  # 특정필드만 사용 시
