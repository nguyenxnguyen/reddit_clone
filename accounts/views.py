from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        info = request.POST
        if info['passwordsignup'] == info['passwordsignup_confirm']:
            if User.objects.filter(username=info['usernamesignup']).exists():
                msg = 'Username already has been taken!'
                return render(request, 'sign_up.html', {'msg': msg})
            else:
                user = User.objects.create_user(info['usernamesignup'], password=info['passwordsignup'])
                login(request, user)
                return render(request, 'sign_up.html')
        else:
            msg = 'Password confirm does not match!'
            username = info['usernamesignup']
            return render(request, 'sign_up.html', {'msg': msg, 'username': username})
    else:
        return render(request, 'sign_up.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST.keys():
                if request.POST['next'] is not None:
                    return redirect(request.POST['next'])
            return redirect('home:index')
        else:
            msg = 'Wrong username or password'
            return render(request, 'log_in.html', {'msg': msg})
    return render(request, 'log_in.html')


def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('home:index')
