from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,ProfilepicForm,LoginForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form1 = ProfilepicForm(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            data = form.save()
            photo = form1.save(commit=False)
            photo.user = data
            photo.save()
            return redirect('login')

    else:
        form = RegisterForm()
        form1 = ProfilepicForm()
    return render(request,'register.html',{'form':form,'form1':form1})

def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            errors = 'Invalid credentials'
            return render(request,'login.html',{'form':form,'errors':errors})
    return render(request,'login.html',{'form':form})

def home(request):
    return HttpResponse('Welcom to home page')