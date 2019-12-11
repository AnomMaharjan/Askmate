from django.db import models

# Create your models here.

class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc= models.TextField()
    question_img = models.ImageField(upload_to="QuestionImg")


class AnswerModel(models.Model):
    posted_by=models.CharField(max_length=120)
    timestamp= models.DateTimeField(auto_now_add=True)
    answer_desc = models.TextField()
    answer_img = models.ImageField(upload_to="AnswerImg")
    is_accepted= models.BooleanField()
    votes= models.IntegerField()
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE) #answer gets deleted if question is deleted 




