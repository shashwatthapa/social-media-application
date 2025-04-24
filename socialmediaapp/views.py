from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,ProfilepicForm
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
    return HttpResponse('Login page')