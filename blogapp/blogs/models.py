from django.db import models
from users.models import User
from taggit.managers import TaggableManager  # 뭐지 ?????????


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
    # ManyToMany : 별도의 테이블로 생성됨
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    # 태그
    tags = TaggableManager()

    def __str__(self):
        return self.title


# 원본글,작성자,내용,작성일시,수정일시
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="원본글")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.user}"
