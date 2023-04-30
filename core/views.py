from django.shortcuts import render
from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login as login_user, logout as logout_user

from .models import UserApp


def index(request):
    return render(request, 'index.html')


def dashbord(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request=request, template_name='dashbord.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='profile.html')
    return redirect('login')


def login(request):

    if request.user.is_authenticated:
        return redirect("profile")

    if (request.POST):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        print(email, password)
        if (user):
            print(user)
            login_user(request, user)
            if (user.role == "Admin"):
                return redirect('dashbord')
            return redirect('profile')
        else:
            data = {'msg': 'email or password are inccorect'}
            return render(request=request, template_name='login.html', context=data)
    else:
        return render(request=request, template_name='login.html')


def register(request):
    if request.POST:
        email = request.POST['email']
        if len(email) <= 8:
            print("invalid email")
        else:
            try:
                user = UserApp.objects.get(email=email)
            except UserApp.DoesNotExist:
                try:
                    user = UserApp.objects.get(username=email[0:8])
                except UserApp.DoesNotExist:
                    user = None
            if user is not None:
                print('email alrelly used')
            else:
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                if len(password) <= 8:
                    print('short password')
                else:
                    if password != cpassword:
                        print("password and Cpassword didn't match")
                    else:
                        first_name = request.POST['first_name']
                        last_name = request.POST['last_name']
                        new_user = UserApp.objects.create(
                            first_name=first_name, last_name=last_name, email=email,
                            is_admin=False, is_active_number=False, is_number=False,
                            username=email[0:8], password=password)
                        new_user.save()
                        login_user(request, new_user)
                        return redirect('second_page_register')
    return render(request=request, template_name='register.html')


def logout(request):
    logout_user(request)
    return redirect('login')
