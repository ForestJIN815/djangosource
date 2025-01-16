from django.db import models

# 모델 (ORM - 클래스와 테이블 1:1 매핑)
# 테이블명을 지정하지 않는다면 앱이름_모델명(ex app1_person)
# 필드 지정
# 문자열 : CharField, TextField
# 숫자 : IntegerField, SmallIntegerField, PositiveIntegerField....
# 날짜 : DateField, DateTimeField, TimeField..
# 이메일 : EmailField
# URL : URLField
# UUID : UUIDField
# IP : GenericIPAddressField
# 파일 : FileField, ImageField, FilePathField
# 참,거짓 : BooleanField

# 관계 : 외래키
# ManyToOne, OneToMany, OneToOne, ManyToMany

# 옵션
# blank, null, default, unique, choices, verbose_name, help_text, validators
# 날짜 타입 옵션
# auto_now_add : 처음에만 날짜/시간 삽입
# auto_now : save() 호출할 때마다 날짜/시간 삽입(최종 수정 시간)


class Person(models.Model):
    # first_name = models.CharField(max_length=30,blank=True,null=True,verbose_name="이름1",unique=True,default="a")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.first_name}"


class Post(models.Model):
    """
    author_name, title, content, is_published(T/F), created_at, updated_at
    """

    author_name = models.CharField(max_length=20, verbose_name="작성자")
    title = models.CharField(max_length=100, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    photo = models.ImageField(blank=True)
    # upload_to : media 아래 폴더 지정
    photo2 = models.ImageField(blank=True, upload_to="blog")
    photo3 = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author_name}"


class Comment(models.Model):
    # 원본글 정보
    # CASCADE : 부모 삭제 시 자식 같이 삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message}"
