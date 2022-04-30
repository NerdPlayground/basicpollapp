from django.db.models import F
from django.urls import reverse
from choices.models import Choice
from questions.models import Question
from questions.forms import QuestionForm
from questions.decorators import is_manager
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect

def unfinished_questions(questions):
    display_questions= list()
    for question in questions:
        if question.choices.all():
            display_questions.append(question)
    return display_questions

def home(request):
    display_questions= list()
    questions= Question.objects.all()
    if request.user.is_authenticated:
        if not request.user.is_manager:
            display_questions= unfinished_questions(questions)
        else:
            display_questions= questions
    else:
        display_questions= unfinished_questions(questions)
    context= {"questions":display_questions}
    return render(request,'questions/home.html',context)

@login_required(login_url="authentication:login-user")
def results(request,pk):
    question= get_object_or_404(Question,pk=pk)
    choices= Choice.objects.filter(question=question)
    context= {
        "question":question,
        "choices":choices
    }
    return render(request,"choices/results.html",context)

@login_required(login_url="authentication:login-user")
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

def question(pk):
    question= get_object_or_404(Question,pk=pk)
    choices= Choice.objects.filter(question=question)
    context= {
        "question":question,
        "choices":choices
    }
    return context

@login_required(login_url="authentication:login-user")
def vote_question(request,pk):
    context= question(pk)
    return render(request,'questions/question.html',context)

@login_required(login_url="authentication:login-user")
@is_manager
def manage_question(request,pk):
    context= question(pk)
    return render(request,'questions/manage_question.html',context)

@login_required(login_url="authentication:login-user")
@is_manager
def add_question(request):
    form= QuestionForm()
    if request.method == "POST":
        form= QuestionForm(request.POST)
        if form.is_valid():
            question= form.save(commit=False)
            question.save()
            return redirect("questions:home")
    context= {"form":form}
    return render(request,"questions/add_question.html",context)

@login_required(login_url="authentication:login-user")
@is_manager
def edit_question(request,pk):
    question= get_object_or_404(Question,pk=pk)
    form= QuestionForm(instance=question)
    if request.method == "POST":
        question.title= request.POST.get('title')
        question.body= request.POST.get('body')
        question.save()
        return redirect(reverse("questions:manage-question",args=(question.id,)))
    context= {"form":form,"question":question.id}
    return render(request,"questions/edit_question.html",context)

@login_required(login_url="authentication:login-user")
@is_manager
def delete_question(request,pk):
    question= get_object_or_404(Question,pk=pk)
    context= {"obj":question}
    if request.method == "POST":
        question.delete()
        return redirect("questions:home")
    return render(request,"delete.html",context)