from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import Member
from .forms import LoginForm

def register(request):
    if request.method == "GET":
        return render(request, 'account/register.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        address = request.POST.get('address', None)


        res_data = {}
        if not (username and password and re_password and email and address and phone and name):
            res_data['error'] = 'Please enter all the values!'

        elif password != re_password:
            res_data['error'] = "The password doesn't match!"
            print(res_data)

        else:
            member = Member (
                username = username,
                email = email,
                password = make_password(password),
                address = address,
                name = name,
                phone = phone,
            )
            member.save()
            return redirect('/shop')

        return render(request, 'account/register.html', res_data)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # session_code 검증하기
            request.session['user'] = form.user_id
            return redirect('/shop')
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form': form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('../../shop')