from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from ending.models import Ending

# Create your views here.
def firstfunc(request):
    return render(request, 'first.html', {})
    # return HttpResponse('kakak')


def loginfunc(request):
    return render(request, 'login.html', {})


def loginfin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('first')


def signupfunc(request):
    return render(request, 'signup.html', {})


def signupfin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, phonenumber, password)
        ending=Ending(base_info ="例）私の名前は・・・",property_info ="例) 年金証書の保管場所は・・・",
            around_info = "例) 使用していたSNSのIDとパスワードは・・・",
            family_info = "例) 私の形見は〇〇に受け取ってほしい・・・",friends_info ="例) 〇〇との思い出は・・・",
            pets_info = "例) ペットの性格は・・・",medical_info = "例) 介護の費用はここから出してほしい・・・",
            inherit_info ="例) 遺言書の保管場所は・・・",contact_info = "例) 私の親友の連絡先は・・・",message_info ="例) ありがとう・・・")
        ending.email=user
        ending.save()
        return redirect('login')


def listfunc(request):
    user_email=request.user
    object = Ending.objects.get(email=user_email)
    return render(request, 'list.html', {'object': object})


def baseshowfunc(request):
    return render(request, 'baseshow.html', {})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def propeditfunc(request):
    object = Ending.objects.all()
    list_object = list(object)[1]
    if request.method == "POST":
        list_object.property_info = request.POST['property_info']
        list_object.save()
        return redirect('list')



