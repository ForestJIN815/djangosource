from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "created_at"]
    inlines = [ChoiceInline]


# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ["choice_text", "votes"]
