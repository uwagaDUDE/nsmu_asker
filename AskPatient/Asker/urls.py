from django.urls import path
from .views import QuestionsView, ThanksView

app_name = 'Asker'

urlpatterns = [
    path('questions', QuestionsView.as_view(), name='patient_questions'),
    path('thank_you', ThanksView.as_view(), name='thanks')
]