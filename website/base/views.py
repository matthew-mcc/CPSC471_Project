from distutils.command.build import build
import re
from urllib.parse import uses_relative
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render
from .forms import RecommendForm, RecoveryForm, SignupForm, LoginForm
from django.contrib.auth.models import User
from .models import CPU, LiquidCooling, AirCooling, MotherBoard, PowerSupply, GPU, Memory, Storage, Case, Build
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def showHome(request):

    return render(request, 'home.html')


def get_cpu(request):
    latest_cpu_list = CPU.objects.all()
    context = {'latest_cpu_list': latest_cpu_list}
    model = request.GET
    print(model.get('model'))
    return render(request, 'cpu.html', context)





def get_gpu(request):
    gpu_list = GPU.objects.all()

    context = {'gpu_list': gpu_list}
    #print(Build.objects.get(build_user=request.user.username))
    print(Build.objects.get(build_user="matt"))
    return render(request, 'gpu.html', context)


def get_motherboard(request):
    motherboard_list = MotherBoard.objects.all()
    context = {'motherboard_list': motherboard_list}
    return render(request, 'motherboard.html', context)


def get_psu(request):
    psu_list = PowerSupply.objects.all()
    context = {'psu_list': psu_list}
    return render(request, 'psu.html', context)


def get_ram(request):
    ram_list = Memory.objects.all()
    context = {'ram_list': ram_list}
    return render(request, 'memory.html', context)


def get_storage(request):
    storage_list = Storage.objects.all()
    context = {'storage_list': storage_list}
    return render(request, 'storage.html', context)


def get_case(request):
    case_list = Case.objects.all()
    context = {'case_list': case_list}
    return render(request, 'case.html', context)


def get_airCool(request):
    ac_list = AirCooling.objects.all()
    context = {'ac_list': ac_list}
    return render(request, 'airCooling.html', context)


def get_liquidCool(request):
    lc_list = LiquidCooling.objects.all()
    context = {'lc_list': lc_list}

    return render(request, 'liquidCooling.html', context)


def showSignUp(request):
    submitbutton = request.POST.get("submit")

    username = ''
    email = ''
    password = ''

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username, email,password)
            #build = Build(build_user=request.user.username)
            #build.save()
            build = Build(build_user=username, name='test', total_price=0, build_cpu='', build_gpu='', build_motherboard='', build_psu='',
                          build_ram='',
                          build_storage1='',
                          build_storage2='',
                          build_case='',
                          build_liquidCooling='',
                          build_airCooling=''
                          )
            build.save()
            return redirect('../signin')
    else:
        form = SignupForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'newaccount.html', context)


def showSignIn(request):
    submitbutton = request.POST.get("submit")
    username = ''
    password = ''

    if request.method == 'POST':
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                print(request.user.username)
                return redirect('../')
            else:
                messages.error(request, "This user does not exist")
                redirect('signin')

    else:
        form = LoginForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'signin.html', context)


def showBuildPage(request):
    return render(request, 'build.html')


def showRecommendedPage(request):
    submitbutton = request.POST.get("submit")

    if request.method == 'POST':
        form = RecommendForm(request.POST)
        if form.is_valid():
            budget = form.cleaned_data.get("budget")
            choice = form.cleaned_data.get("choice")
    else:
        form = RecommendForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'recommend.html', context)


def showRecoveryPage(request):
    submitbutton = request.POST.get("submit")
    email = ''
    password = ''
    if request.method == 'POST':
        form = RecoveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            try:
                user = User.objects.get(email=email)
                password = user.password
                subject = 'Monkee PC Builder Password Recovery'
                message = 'Hey there, You forgot your password, here it is!\n'
                message += 'Password: ' + password
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject=subject, message=message,
                          from_email=email_from, recipient_list=recipient_list)
                return redirect('../')
            except User.DoesNotExist:
                messages.error(request, "This is email is not registered!")
    else:
        form = RecoveryForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'recovery.html', context)
