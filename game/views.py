from django.shortcuts import render
import random

# Create your views here.
def start(request):
    return render(request, 'start.html')

def role(request):
    role=['lion','alligator', 'chameleon', 'deer', 'eagle', 'hyena', 'snake', ]
    random_role = random.choice(role)
    return render(request, 'role.html', {'role':random_role})


def choose_area(request):
    return render(request, 'choose_area.html')

def area_people(request):
    return render(request, 'area_people.html')

def result(request):
    return render(request, 'result.html')