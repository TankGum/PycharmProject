from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    myname = "tankgum"
    items = ["phone", "laptop", "bike"]
    context = {"name": myname, "items": items}
    return render(request, "polls/index.html", context)

def view_list(request):
    list_question = Question.objects.all()
    context = {"list question": list_question}
    return render(request, "polls/question_list.html", context)

def detail_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail_question.html", context)
