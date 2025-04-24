from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.
def register(request):
    form = RegisterForm()
    return render(request,'register.html',{'form':form})
