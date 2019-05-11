from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, 'start.html')

def role(request):
    return render(request, 'role.html', {'role':role})


def choose_area(request):
    return render(request, 'choose_area.html')

def area_people(request):
    return render(request, 'area_people.html')

def result(request):
    return render(request, 'result.html')