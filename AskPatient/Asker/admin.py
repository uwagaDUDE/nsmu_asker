from django.contrib import admin
from .models import Questions, Doctor, AvailabaleAnswers, Answers, Comments
# Register your models here.

class AnswersAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'question', 'answer', 'answer_date']
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    verbose_name = 'Вопрос'
    verbose_name_plural = 'Вопросы'

class DoctorAdmin(admin.ModelAdmin):
    verbose_name = 'Врач'
    verbose_name_plural = 'Врачи'
    list_display = ['name']

class AvailableAnswersAdmin(admin.ModelAdmin):
    list_display = ['av_answer']
    verbose_name = 'Доступный ответ'
    verbose_name_plural = 'Доступные ответы'


class CommentsAdmin(admin.ModelAdmin):
    def __str__(self):
        return "Комментарий"
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'
    
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(AvailabaleAnswers, AvailableAnswersAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Answers, AnswersAdmin)