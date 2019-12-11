from django.shortcuts import render
from .models import QuestionModel


def addquestion(request):
    question = QuestionModel.objects.all()
    return render(request, "newquestion.htm", {"questions": question})
