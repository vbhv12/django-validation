from django.shortcuts import render
from django import forms
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request,'basicapp/index.html')


def user(request):
    form=newuserform()

    if request.method=="POST":
        form=newuserform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('error form')

    return render(request,'basicapp/form.html',{'form':form})


   