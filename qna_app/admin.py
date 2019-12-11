from django.contrib import admin
from .models import QuestionModel, AnswerModel

admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
