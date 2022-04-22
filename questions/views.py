from django.db.models import F
from django.urls import reverse
from choices.models import Choice
from questions.models import Question
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

def home(request):
    questions= Question.objects.all()
    context= {"questions":questions}
    return render(request,'questions/home.html',context)

def results(request,pk):
    question= get_object_or_404(Question,pk=pk)
    choices= Choice.objects.filter(question=question)
    context= {
        "question":question,
        "choices":choices
    }
    return render(request,"choices/results.html",context)

def vote(request,pk):
    question= get_object_or_404(Question,pk=pk)
    try:
        choice= Choice.objects.filter(question=question).get(id=request.POST.get('choice'))
        choice.votes= F("votes") + 1
        choice.save()
        return HttpResponseRedirect(reverse("questions:results",args=(question.id,)))
    except(KeyError, Choice.DoesNotExist):
        choices= Choice.objects.filter(question=question)
        context= {
            "question":question,
            "choices":choices,
            "error_message":"You didn't select a choice."
        }
        return render(request,'questions/question.html',context)

def question(request,pk):
    question= get_object_or_404(Question,pk=pk)
    choices= Choice.objects.filter(question=question)
    context= {
        "question":question,
        "choices":choices
    }
    return render(request,'questions/question.html',context)