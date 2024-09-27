from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        add_todo = Todo(user=request.user,title=title,description=description,created_date=date)
        add_todo.save()
        messages.success(request,'Created')
        return redirect('home-page')
    all_todo =Todo.objects.filter(user=request.user)
    return render(request,'todo.html',{'all_todo':all_todo})

def logout_view(request):
    logout(request)
    return redirect('login') 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(password) < 4 :
            messages.error(request,'Password must be at least 4 characters')
            return redirect('register')
        get_all_user_by_username = User.objects.filter(username=username)
        if get_all_user_by_username:
            messages.error(request,'Username already exist')
            return redirect('register')
        messages.success(request,"User successfully created, Login now ")
        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        return redirect('login')
    return render(request,"register.html",{})

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    return render(request,"login.html",{})


def delete(request,title):
    get_todo = Todo.objects.get(user=request.user,title=title)
    get_todo.delete()
    return redirect('home-page')
def update(request,title):
    get_todo = Todo.objects.get(user=request.user,title=title)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')