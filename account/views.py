from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_details = request.POST
        fnm=user_details.get('first_name')
        lnm=user_details.get('last_name')
        email=user_details.get('email')
        unm=user_details.get('username')
        psw=user_details.get('password')
        re_psw=user_details.get('confirm_password')
        if psw==re_psw:
            user=User.objects.create_user(unm,email,psw)
            user.save()
            
            return HttpResponseRedirect('/account/login/')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def logIn(request):
    form_data=request.POST
    nm=form_data.get('username')
    psw=form_data.get('password')
    user = authenticate(username=nm, password=psw)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect('/account/home/')
    else:
        return render(request, 'logIn.html')

def home(request):
    print "in home "
    user = request.user.username
    print user
    return render(request, 'home.html', {'name' : user})


def logOut(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')