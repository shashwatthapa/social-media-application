from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,ProfilepicForm,LoginForm,PostForm
from django.contrib.auth import login,logout,authenticate
from .models import Post
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
    mem = Post.objects.all().order_by('-id')
    return render(request,'home.html',{'mem':mem})

def user_logout(request):
    logout(request)
    return redirect('login')

def post(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
        return render(request,'post.html',{'form':form})

def own_post(request):
    mem = Post.objects.filter(user=request.user)
    return render(request,'own_post.html',{'mem':mem})

    