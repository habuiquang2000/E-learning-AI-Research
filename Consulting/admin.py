from django import forms
from django.contrib import admin
from .models import Question, Answer

# Register your models here.


class AnswerModelForm(forms.ModelForm):
    keyword = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Answer
        fields = '__all__'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    form = AnswerModelForm
    list_display = (
        "content",
        "keyword",
        "created",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "user",
        "created",
    )
