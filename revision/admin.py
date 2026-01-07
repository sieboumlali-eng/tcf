from django.contrib import admin
from .models import ExamOrale, QuestionOrale

class QuestionOraleInline(admin.StackedInline):
    model = QuestionOrale
    extra = 1

@admin.register(ExamOrale)
class ExamOraleAdmin(admin.ModelAdmin):
    inlines = [QuestionOraleInline]
    list_display = ('number_exam_orale', 'description_exam_orale')

@admin.register(QuestionOrale)
class QuestionOraleAdmin(admin.ModelAdmin):
    list_display = ('num_qst', 'exam', 'text_qst')
