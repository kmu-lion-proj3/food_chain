
from django.shortcuts import render,redirect, get_object_or_404
from .models import Animal
from django.contrib.auth.models import User
# from .models import Post
from django.contrib import auth
import random

# Create your views here.
def start(request):
    return render(request, 'start.html')

def role(request):
    role=['lion','alligator', 'chameleon', 'deer', 'eagle', 'hyena', 'snake','crocodile_bird','crow','mallard','mouse','otter','rabbit' ]
    random_role = random.choice(role)
    address = 'image/role/'+str(random_role)+'.png'
    return render(request, 'role.html', {'role':random_role, 'address':str(address)})


def choose_area(request):
    return render(request, 'choose_area.html')

def area_people(request):
    return render(request, 'area_people.html')

def result(request):
    return render(request, 'result.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('start')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                   username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
               

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('start')
