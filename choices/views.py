from django.urls import reverse
from choices.models import Choice
from django.contrib import messages
from questions.models import Question
from choices.forms import ChoicesForm
from questions.decorators import is_manager
from django.http import Http404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

@login_required(login_url="authentication:login-user")
@is_manager
def add_choice(request,pk):
    form= ChoicesForm()
    question= Question.objects.get(id=pk)
    if request.method == "POST":
        form= ChoicesForm(request.POST)
        if form.is_valid():
            choice= form.save(commit=False)
            choice.question=question
            choice.save()
            return redirect(reverse("questions:manage-question",args=(pk,)))
    context= {"form":form,"question":question.id}
    return render(request,"choices/add_choice.html",context)

@login_required(login_url="authentication:login-user")
@is_manager
def edit_choice(request,pk):
    choice= get_object_or_404(Choice,pk=pk)
    form= ChoicesForm(instance=choice)
    if request.method == "POST":
        choice.body= request.POST.get('body')
        choice.save()
        return redirect(reverse("questions:manage-question",args=(choice.question.id,)))
    context={"form":form,"question":choice.question.id}
    return render(request,"choices/edit_choice.html",context)

@login_required(login_url="authentication:login-user")
@is_manager
def delete_choice(request,pk):
    choice= get_object_or_404(Choice,pk=pk)
    context= {"obj":choice}
    if request.method == "POST":
        choice.delete()
        return redirect(reverse("questions:manage-question",args=(choice.question.id,)))
    return render(request,"delete.html",context)