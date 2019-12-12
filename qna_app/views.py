from django.shortcuts import render, redirect
from .models import QuestionModel, CategoryModel
from .forms import QuestionForm
from .models import QuestionModel
from django.http import HttpResponse
from django.views.generic import CreateView, ListView




def addquestion(request):
    # q = CategoryModel.objects.create(category_title='General', category_despcription='Any kinds of questions')
    # question = QuestionModel.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                return redirect('qna:questionlist')
            except:
                return HttpResponse("Failed")

        else:
            print(form.errors)
            return HttpResponse(form.errors)

    else:
        form = QuestionForm
        category = CategoryModel.objects.all()
        return render(request, "questionmodel_create.htm", {'category': category})


def update_question(request, id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":

        form = QuestionForm(request.POST, request.FILES, instance=question)

        if form.is_valid():
            try:

                form.save()
                return redirect('qna:update', id)

            except:
                return HttpResponse("Failed")

        else:
            return HttpResponse(form.errors)

    else:
        form = QuestionForm(instance=question)
        return render(request, "questionmodel_update.htm", {'form': form})


def questionlist(request):
    lists = QuestionModel.objects.all()
    return render(request, "questionmodel_list.htm", {"question_list": lists})


def delete_question(requests, id):
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:questionlist')

class QuestionModelCreateView(CreateView):
    model= QuestionModel
    fields = "__all__"

class QuestionModelListView(ListView):
    model= QuestionModel
    queryset= QuestionModel.objects.all()

def upvote(request,id):
    instance=QuestionModel.objects.get(id=id)
    vote=instance.question_vote + 1
    instance.question_vote =vote
    instance.save()
    redirect("qna:questionlist")
