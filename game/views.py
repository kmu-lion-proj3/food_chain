
from django.shortcuts import render,redirect, get_object_or_404
from .models import Animal
from django.contrib.auth.models import User
# from .models import Post
from django.contrib import auth
import random


# Create your views here.
def start(request):
    # role_array=['lion','alligator', 'chameleon', 'deer', 'eagle', 'hyena', 'snake','crocodile_bird','crow','mallard','mouse','otter','rabbit' ]
    # random.shuffle(role_array)
    # animal_object_list=[]
    
    # for temp in role_array:
    #     item = Animal.objects.get(kind=temp)
    #     item.ID= None
    #     item.save()
    #     animal_object_list.append(item)
    
    # index=0
    # for user in User.objects.all():
    #     animal_object_list[index].id_update(user)
    #     index+=1
    return render(request, 'start.html', )

def role(request):
    # role_array=['lion','alligator', 'chameleon', 'deer', 'eagle', 'hyena', 'snake','crocodile_bird','crow','mallard','mouse','otter','rabbit' ]
    # random_role = random.choice(role_array)
    # temp = Animal.objects.get(kind=random_role)
    # request.user.animal=temp
    # # role_array.remove(random_role)
    # address = 'image/role/'+str(random_role)+'.png'
    role_array=['lion','alligator', 'chameleon', 'deer', 'eagle', 'hyena', 'snake','crocodile_bird','crow','mallard','mouse','otter','rabbit' ]
    random.shuffle(role_array)
    animal_object_list=[]
    
    for temp in role_array:
        item = Animal.objects.get(kind=temp)
        item.ID= None
        item.save()
        animal_object_list.append(item)
    
    index=0
    for user in User.objects.all():
        animal_object_list[index].id_update(user)
        index+=1
    
    # user의 동물 받아오기
    kind = request.user.animal
    address = 'image/role/'+str(kind.kind)+'.png'
    
    # user의 동물 받아오기 end
    # kind.id_update(request.user)
    return render(request, 'role.html', {'address':str(address),
                                        'your_kind':kind,
                                        'a_list':animal_object_list,
                                        })


def choose_area(request):

    kind = request.user.animal
    return render(request, 'choose_area.html', {'kind':kind})

def choose_process(request):
    request.user.animal.location=request.GET['area']
    
    return redirect('area_people')

def area_people(request):
    place = request.user.animal.location
    allobject=Animal.objects.filter(location=place)
    return render(request, 'area_people.html',{'allobject':allobject})

def result(request):
    return render(request, 'result.html')


# account 관련 액션
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
