from questions.models import Question
from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect

def all_questions(request):
    questions= Question.objects.all()
    context= {"questions":questions}
    return render(request,'questions/all-questions.html',context)

def question(request,pk):
    try:
        question= Question.objects.get(id=pk)
        context= {"question":question}
        return render(request,'questions/question.html',context)
    except Question.DoesNotExist:
        raise Http404