from django.db import models

# 설문조사 앱
# 질문 / 선택 답변


# 질문 : 번호, 질문내용, 작성일
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


# 답변 : 외래키, 답변내용, 투표수
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
