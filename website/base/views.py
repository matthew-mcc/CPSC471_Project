from django.http import HttpResponse
from django.shortcuts import render
from .forms import RecommendForm, SignupForm, LoginForm
from django.contrib.auth.models import User
from .models import CPU, User

def showHome(request):

    return render (request, 'home.html')


def get_cpu(request):
    latest_cpu_list = CPU.objects.all()
    
    context = {'latest_cpu_list': latest_cpu_list}
    return render(request, 'index.html', context)



def showSignUp(request):
    submitbutton = request.POST.get("submit")

    username =''
    email = ''
    password = ''

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            #newUser = User.objects.create_user(username,email,password)
            newUser = User(username=username, email=email, password=password)
            newUser.save()
    else:
        form = SignupForm()
    context = {'form':form, 'submitbutton': submitbutton}
    return render(request, 'newaccount.html', context)


def showSignIn(request):
    submitbutton = request.POST.get("submit")

    username =''
    password = ''

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            #newUser = User.objects.create_user(username,email,password)

        
    else:
        form = SignupForm()
    context = {'form':form, 'submitbutton': submitbutton}
    return render(request, 'signin.html', context)


def showBuildPage(request):
    return render (request, 'build.html')

def showRecommendedPage(request):
    submitbutton = request.POST.get("submit")

    if request.method == 'POST':
        form = RecommendForm(request.POST)
        if form.is_valid():
            budget = form.cleaned_data.get("budget")
            choice = form.cleaned_data.get("choice")
    else:
        form = RecommendForm()
    context = {'form':form, 'submitbutton':submitbutton}
    return render (request, 'recommend.html', context)
