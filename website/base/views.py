from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RecommendForm, SignupForm, LoginForm
from django.contrib.auth.models import User
from .models import CPU, LiquidCooling, AirCooling, MotherBoard, PowerSupply, User, GPU, Memory, Storage, Case

def showHome(request):

    return render (request, 'home.html')


def get_cpu(request):
    latest_cpu_list = CPU.objects.all()
    
    context = {'latest_cpu_list': latest_cpu_list}
    return render(request, 'cpu.html', context)

def get_gpu(request):
    gpu_list = GPU.objects.all()
    
    context = {'gpu_list': gpu_list}
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

    #test = LiquidCooling(model_name='is this here?', price=1000, radiator_size='a', location='b')
    #test.save()

    return render(request, 'liquidCooling.html', context)

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
            newUser = User.objects.create_user()
            newUser = User(username=username, email=email, password=password)
            newUser.save()
            return redirect('../signin')
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
