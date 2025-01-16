from django.db import models


class Book(models.Model):
    """
    code(숫자),title,author,price(숫자),created_at
    """

    code = models.IntegerField(
        verbose_name="도서코드", unique=True, help_text="코드는 숫자 4자리로 작성하세요"
    )
    title = models.CharField(max_length=200, verbose_name="도서명")
    author = models.CharField(max_length=100, verbose_name="저자")
    price = models.IntegerField(
        verbose_name="도서가격", help_text="최소 1000 이상이어야 합니다."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일시")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "booktbl"
