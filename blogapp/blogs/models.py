from django.db import models
from users.models import User


# 번호(자동생성), user, 제목(title), 내용(content), image(option), 작성날짜(created_at), 수정날짜(modified_at)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    # /media/image 사용
    image = models.ImageField(
        blank=True, null=True, verbose_name="첨부파일", upload_to="image"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
