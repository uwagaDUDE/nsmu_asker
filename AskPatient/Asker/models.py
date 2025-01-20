from django.db import models
import uuid

from django.utils import timezone
from django.core.exceptions import ValidationError
class Questions(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.CharField(verbose_name='Вопрос', unique=True)
    active = models.BooleanField(verbose_name='Активность', default=True)
    
    def __str__(self):
        return self.question_text


class Doctor(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='ФИО Врача', unique=True)
    
    def __str__(self):
        return self.name

    
class AvailabaleAnswers(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    av_answer = models.IntegerField(verbose_name='Ответ', unique=True) # Только цифры
    
    def __str__(self):
        return str(self.av_answer)
    
class Answers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.CharField(verbose_name='Пациент', max_length=255)  # Добавьте max_length
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name="Вопрос")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    answer = models.ForeignKey(AvailabaleAnswers, on_delete=models.CASCADE, verbose_name="Ответ")
    answer_date = models.DateField(verbose_name="Дата ответа", default=timezone.now)

    @property
    def doc_fio(self):
        return self.doctor.name if self.doctor else None

    @property
    def doc_questions(self):
        return self.question.question_text if self.question else None

    @property
    def answers(self):
        return self.answer.av_answer if self.answer else None

    def __str__(self):
        return f"Вопрос: {self.question.question_text}| Ответ: {self.answer.av_answer}"

class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField(verbose_name='Коммент', blank=True, null=True, max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    
    @property
    def doc_fio(self):
        return self.doctor.name if self.doctor else None
    
    def __str__(self):
        return "Комментарии"
