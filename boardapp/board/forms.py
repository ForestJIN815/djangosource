from django import forms
from .models import Question, Answer, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
