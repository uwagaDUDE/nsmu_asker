from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.staticfiles import finders
import os
from .scripts import upload_answer

from .models import Questions, AvailabaleAnswers, Answers, Doctor, Comments

class QuestionsView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "questions":Questions.objects.filter(active=True),
            "doctors":Doctor.objects.all(),
            "answers":AvailabaleAnswers.objects.all()
        })
        return context
    
    def post(self, request):
        if 'send_answer' in request.POST:
            answer = upload_answer(
                request=request,
                answers_db=Answers,
                comments_db=Comments,
                doctor_db=Doctor,
                questions_db=Questions,
                av_answerd_db=AvailabaleAnswers)
            print(answer)
        return redirect('Asker:thanks')
    
class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context