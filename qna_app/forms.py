from django import forms
from .models import QuestionModel, AnswerModel, CategoryModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model= CategoryForm
#         fields='__all__'

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model= AnswerForm
#         fields='__all__'
