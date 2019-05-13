
from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, Situation
from django.contrib.auth.models import User
# from .models import Post
from django.contrib import auth
import random

round
# Create your views here.


def start(request):
    return render(request, 'start.html', )


def role(request):
    if request.user.username == 'chulhee23@likelion.org':
        global round
        round = 0
        # admin 계정이면 새로 게임 시작시 모든 상황 모델 데이터 날리기
        Situation.objects.all().delete()

        role_array = ['lion', 'alligator', 'chameleon', 'deer', 'eagle', 'hyena',
                      'snake', 'crocodile_bird', 'crow', 'mallard', 'mouse', 'otter', 'rabbit']
        random.shuffle(role_array)
        animal_object_list = []

        for temp in role_array:
            item = Animal.objects.get(kind=temp)
            item.ID = None
            item.life = True
            # if item.kind=='lion':
            #     item.starve=1
            item.save()
            animal_object_list.append(item)

        index = 0
        for user in User.objects.all():
            animal_object_list[index].id_update(user)
            index += 1
        game_open = "game restart!"
    else:
        game_open = "game 진행중..."
    # user의 동물 받아오기
    kind = request.user.animal
    address = 'image/role/'+str(kind.kind)+'.png'

    # user의 동물 받아오기 end
    # kind.id_update(request.user)
    return render(request, 'role.html', {'address': str(address),
                                         'your_kind': kind,
                                         'round': round,
                                         'game_open': game_open
                                         })


def choose_area(request):
    if request.user.animal.life == False:
        return redirect('endgame')
    
    global round
    if round ==4:
        winners = Animal.objects.filter(life = True)
        return render(request, 'final.html',{'winners': winners})

    round += 1
    kind = request.user.animal
    return render(request, 'choose_area.html', {'kind': kind})


def choose_process(request):
    place = request.GET['area']
    request.user.animal.location_update(place)
    return redirect('area_people')


def area_people(request):
    place = request.user.animal.location
    allobject = Animal.objects.filter(location=place, life=True)
    return render(request, 'area_people.html', {'allobject': allobject})


def situation_create(request):
    # 모든 공격이 이뤄지면 모든 동물은 starve -= 1
    request.user.animal.starve -= 1

    # situation에 공격 상황 및 라운드 기록
    global round

    situation = Situation()
    situation.attacker = request.user
    attacked_user = request.GET['animal']
    temp = User.objects.get(username=attacked_user)
    situation.attacked = temp

    # 공격을 하지 않을 경우 상황 저장 X
    if situation.attacked != situation.attacker:
        situation.round = round
        situation.location = request.user.animal.location
        situation.save()

    attacker = situation.attacker.animal
    attacked = situation.attacked.animal
    

    # status 및 조건에 따른 공격 성공 여부 확인
    if attacker.status > attacked.status:
        attacked.life = False
        attacker.starve += 1
        attacker.save()
        attacked.save()
    elif attacker==attacked:
        return redirect('result', round)
    else:
        attacker.life = False
        attacker.save()
    return redirect('result' , round)

def result(request,round):
    round = round
    all_situation = Situation.objects.filter(round=round, location=request.user.animal.location)
    return render(request, 'result.html', {'situation': all_situation, 'round': round})


def endgame(request):
    return render(request, 'endgame.html')

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
