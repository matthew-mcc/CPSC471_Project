from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User

def showHome(request):

    return render (request, 'home.html')

def showSignUp(request):
    submitbutton = request.POST.get("submit")

    username =''
    email = ''
    password = ''

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            #newUser = User.objects.create_user(username,email,password)
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
        if(form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            #newUser = User.objects.create_user(username,email,password)
    else:
        form = SignupForm()
        context = {'form':form, 'submitbutton': submitbutton}
        return render(request, 'signin.html', context)