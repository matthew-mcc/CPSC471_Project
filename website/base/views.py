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
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def showHome(request):
    if request.user.username == None:
        context = {'current_user':'guest'}
    else:
        context = {'current_user':request.user.username}
    return render(request, 'home.html', context)


def get_cpu(request):
    latest_cpu_list = CPU.objects.all()
    context = {'latest_cpu_list': latest_cpu_list}
    model = request.GET
    cpu = Build.objects.get(build_user=request.user.username)
    cpu.build_cpu = model.get('model')
    if cpu.build_cpu is not None:
        cpu.save()
    return render(request, 'cpu.html', context)


def get_gpu(request):
    gpu_list = GPU.objects.all()

    context = {'gpu_list': gpu_list}
    model = model = request.GET
    gpu = Build.objects.get(build_user=request.user.username)
    gpu.build_gpu = model.get('model')
    if gpu.build_gpu is not None:
        gpu.save()
    # return redirect('../build')

    return render(request, 'gpu.html', context)


def get_motherboard(request):
    motherboard_list = MotherBoard.objects.all()
    context = {'motherboard_list': motherboard_list}
    model = model = request.GET
    mobo = Build.objects.get(build_user=request.user.username)
    mobo.build_motherboard = model.get('model')
    if mobo.build_motherboard is not None:
        mobo.save()
    return render(request, 'motherboard.html', context)


def get_psu(request):
    psu_list = PowerSupply.objects.all()
    context = {'psu_list': psu_list}
    model = model = request.GET
    psu = Build.objects.get(build_user=request.user.username)
    psu.build_psu = model.get('model')
    if psu.build_psu is not None:
        psu.save()
    return render(request, 'psu.html', context)


def get_ram(request):
    ram_list = Memory.objects.all()
    context = {'ram_list': ram_list}
    model = model = request.GET
    ram = Build.objects.get(build_user=request.user.username)
    ram.build_ram = model.get('model')
    if ram.build_ram is not None:
        ram.save()
    return render(request, 'memory.html', context)


def get_storage(request):
    storage_list = Storage.objects.all()
    context = {'storage_list': storage_list}
    model = model = request.GET
    storage = Build.objects.get(build_user=request.user.username)
    storage.build_storage1 = model.get('model')
    if storage.build_storage1 is not None:
        storage.save()
    return render(request, 'storage.html', context)


def get_storage2(request):
    storage_list = Storage.objects.all()
    context = {'storage_list': storage_list}
    model = model = request.GET
    storage = Build.objects.get(build_user=request.user.username)
    storage.build_storage2 = model.get('model')
    if storage.build_storage2 is not None:
        storage.save()
    return render(request, 'storage2.html', context)


def get_case(request):
    case_list = Case.objects.all()
    context = {'case_list': case_list}
    model = model = request.GET
    case = Build.objects.get(build_user=request.user.username)
    case.build_case = model.get('model')
    if case.build_case is not None:
        case.save()
    return render(request, 'case.html', context)


def get_airCool(request):
    ac_list = AirCooling.objects.all()
    context = {'ac_list': ac_list}
    model = model = request.GET
    air = Build.objects.get(build_user=request.user.username)
    air.build_airCooling = model.get('model')
    if air.build_airCooling is not None:
        air.save()
    return render(request, 'airCooling.html', context)


def get_liquidCool(request):
    lc_list = LiquidCooling.objects.all()
    context = {'lc_list': lc_list}
    model = model = request.GET
    liquid = Build.objects.get(build_user=request.user.username)
    liquid.build_liquidCooling = model.get('model')
    if liquid.build_liquidCooling is not None:
        liquid.save()
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
            if User.objects.filter(username = username).exists():
                return redirect('signup')
            else:
                user = User.objects.create_user(username, email,password)
                build = Build(build_user=username, name=username+"'s Build", total_price=0, build_cpu='', build_gpu='', build_motherboard='', build_psu='',
                            build_ram='',
                            build_storage1='',
                            build_storage2='',
                            build_case='',
                            build_liquidCooling='',
                            build_airCooling=''
                            )
                build.save()
                messages.success(request,"Account Registered!")
                return redirect('../signin')
    else:
        form = SignupForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'newaccount.html', context)


def showSignIn(request):
    submitbutton = request.POST.get("submit")
    username = ''
    password = ''
    msg = ''
    if request.method == 'POST':
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                msg += "Hello " + username + "!"
                messages.success(request, msg)
                return redirect('../')
            else:
                messages.error(request, "This user does not exist")
                redirect('signin')

    else:
        form = LoginForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'signin.html', context)


def showBuildPage(request):
    build = Build.objects.get(build_user=request.user.username)
    prices = {}
    sum = 0
    if build.build_cpu != '':
        cpu = CPU.objects.get(model_name=build.build_cpu)
        prices['cpu'] = cpu.price
        sum += cpu.price
    if build.build_gpu != '':
        gpu = GPU.objects.get(model_name = build.build_gpu)
        prices['gpu'] =gpu.price
        sum += gpu.price
    if build.build_motherboard != '':
        motherboard = MotherBoard.objects.get(model_name = build.build_motherboard)
        sum += motherboard.price
        prices['mobo'] = motherboard.price
    if build.build_psu != '':
        psu = PowerSupply.objects.get(model_name = build.build_psu)
        prices['psu'] = psu.price
        sum += psu.price
    if  build.build_ram != '':
        ram = Memory.objects.get(model_name = build.build_ram)
        prices['ram'] =ram.price
        sum += ram.price
    if  build.build_storage1 != '':
        storage = Storage.objects.get(model_name = build.build_storage1)
        prices['stor1'] =storage.price
        sum += storage.price
    if build.build_storage2 != '':
        storage2 = Storage.objects.get(model_name = build.build_storage2)
        prices['stor2'] =storage2.price
        sum += storage2.price
    if build.build_case != '':
        case = Case.objects.get(model_name = build.build_case)
        prices['case'] =case.price
        sum += case.price
    if build.build_liquidCooling != '':
        liquid = LiquidCooling.objects.get(model_name = build.build_liquidCooling)
        prices['lc'] =liquid.price
        sum += liquid.price
    if build.build_airCooling != '':
        air = AirCooling.objects.get(model_name = build.build_airCooling)
        prices['ac'] =air.price
        sum += air.price


    context = {'build': build, 'prices': prices, 'sum':sum}
    return render(request, 'build.html', context)


def getRecommendedBuild(budget, choice):
    budget = int(budget)
    choice = int(choice)
    
    if choice == 1: # gaming
        if budget > 1500:
            return("High Level Gaming Recommendation")
        if budget < 1500:
            return("Low Level Gaming Recommendation")
    if choice == 2: # streaming 
        if budget > 1500:
            return("High Level Streaming Recommendation")
        if budget < 1500:
            return("Low Level Streaming Recommendation")
    if choice == 3: # office
        if budget > 1500:
            return("High Level Office Recommendation")
        if budget < 1500:
            return("Low Level Office Recommendation")
    else:
        print("Bad Choice") # debugging 
        

def showRecommendedPage(request):
    submitbutton = request.POST.get("submit")

    if request.method == 'POST':
        form = RecommendForm(request.POST)
        if form.is_valid():

            budget = form.cleaned_data.get("budget")
            choice = form.cleaned_data.get("choice")
            
            build_name = getRecommendedBuild(budget, choice)
            
            global getRecBuildName
            def getRecBuildName():
                return build_name

            return redirect('../recommendBuild')
    else:
        form = RecommendForm()
    context = {'form': form, 'submitbutton': submitbutton}
    return render(request, 'recommend.html', context)

def renderRecommendedBuild(request):

    #get the build (make it in here)
    recBuildName = getRecBuildName()
    build = Build.objects.get(name=recBuildName)
    prices = {}
    sum = 0
    if build.build_cpu != '':
        cpu = CPU.objects.get(model_name=build.build_cpu)
        prices['cpu'] = cpu.price
        sum += cpu.price
    if build.build_gpu != '':
        gpu = GPU.objects.get(model_name = build.build_gpu)
        prices['gpu'] =gpu.price
        sum += gpu.price
    if build.build_motherboard != '':
        motherboard = MotherBoard.objects.get(model_name = build.build_motherboard)
        sum += motherboard.price
        prices['mobo'] = motherboard.price
    if build.build_psu != '':
        psu = PowerSupply.objects.get(model_name = build.build_psu)
        prices['psu'] = psu.price
        sum += psu.price
    if  build.build_ram != '':
        ram = Memory.objects.get(model_name = build.build_ram)
        prices['ram'] =ram.price
        sum += ram.price
    if  build.build_storage1 != '':
        storage = Storage.objects.get(model_name = build.build_storage1)
        prices['stor1'] =storage.price
        sum += storage.price
    if build.build_storage2 != '':
        storage2 = Storage.objects.get(model_name = build.build_storage2)
        prices['stor2'] =storage2.price
        sum += storage2.price
    if build.build_case != '':
        case = Case.objects.get(model_name = build.build_case)
        prices['case'] =case.price
        sum += case.price
    if build.build_liquidCooling != '':
        liquid = LiquidCooling.objects.get(model_name = build.build_liquidCooling)
        prices['lc'] =liquid.price
        sum += liquid.price
    if build.build_airCooling != '':
        air = AirCooling.objects.get(model_name = build.build_airCooling)
        prices['ac'] =air.price
        sum += air.price
    context = {'build':build, 'prices':prices, 'sum': sum}
    return render(request, 'recommendBuild.html', context)

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
