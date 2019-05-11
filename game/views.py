from django.shortcuts import render
import random

# Create your views here.
def start(request):
    return render(request, 'start.html')

def role(request):
    num = random.randint(0,12)
    return render(request, 'role.html')


def choose_area(request):
    return render(request, 'choose_area.html')

def area_people(request):
    return render(request, 'area_people.html')

def result(request):
    return render(request, 'result.html')