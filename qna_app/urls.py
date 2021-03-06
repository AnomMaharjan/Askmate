"""askmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

app_name='qna'

urlpatterns = [
    path('addquestion/', addquestion, name='addquestion'),
    path('update/<int:id>/',update_question,name="update"),
    path('read/', questionlist, name="read"),
    path('delete/<int:id>', delete_question, name='delete'),
    path('create/', QuestionModelCreateView.as_view(), name="create"),
    path('listview/', QuestionModelListView.as_view(), name="listview"),
    path('upvote/<int:id>',upvote, name="upvote"),
    path('submit/<int:id>', addanswer, name="addanswer"),
    path('detail/<int:id>', details, name="detail"),
    path('base/', base, name='base'),
    path('lists/',ques_list,name="lists"),
    path('ques_details/<int:id>',ques_details,name='ques_details')
]
