from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from .form import CustomUserForm
from .models import Message_Feedback
from seller.models import Personal_Info
from django.core.signing import Signer


def home(request):
    return render(request, 'homes/home.html')

def choice(request):
    return render(request, 'account/decisions.html')

def profile(request):
    return render(request, 'account/decision.html')

    
def metas(request):
    some = Personal_Info(profile = request.user)
    signer = Signer()
    value = signer.sign(request.user)
    context = {
        "u_token": value
    }
    if some.is_seller == False:
        return render(request, 'profile/profile.html', context)
    return render(request, 'account/decisions.html', context)

def projects(request):
    some = Personal_Info(profile = request.user)
    value = request.user
    context = {
        "u_token": value
    }
    if some.is_seller == False:
        return render(request, 'profile/profile.html', context)
    return render(request, 'account/decisions.html', context)

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subcribe = request.POST.get('subcribe')
        if subject == "":
            return JsonResponse({"yemi": "Subject can't be empty, we will use your subject for our teams to response faster", "state": "info", "msg": "Info"})
        if email == "":
            return JsonResponse({"yemi": "Email can't be empty, we will need youe email to get back to you", "state": "info", "msg": "Info"})
        if message == "":
            return JsonResponse({"yemi": "Message can't be empty, message is important.", "state": "info", "msg": "Info"})
        if subcribe == "true":
            feedback = Message_Feedback(name=name, subject=subject, email=email, message=message, subscribe=True)
            feedback.save()
        else:
            feedback = Message_Feedback(name=name, subject=subject, email=email, message=message, subscribe=False)
            feedback.save()
        return JsonResponse({"yemi": "Subscribe Successfully", "state": "success", "msg": "Success"})

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'registered successfully! login to continue')
            return redirect('/login/')
    context = {'form': form}
    return render(request, 'account/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username', None)
            passwd = request.POST.get('passwd', None)
            if name is not None and passwd is not None:
                user = authenticate(request, username=name, password=passwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in sucessfully')
                    return redirect("/")
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('/login/')
        return render(request, 'account/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
    return redirect('/')
