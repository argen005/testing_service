from django.contrib import admin
from .models import TestSet, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

@admin.register(TestSet)
class TestSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title', 'description')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('id', 'text', 'test_set')
    list_filter = ('test_set',)
    list_display_links = ('text', 'test_set')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'is_correct')
    list_display_links = ('text', 'question')
