from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

import sweetify
# Create your views here.

def sign_up(request):
    if not request.user.is_authenticated:  # if user logged in then block signup from url
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
            
                sweetify.success(request, 'User created successfully. Please Login', persistent='Close')
            
                return redirect('/')


        else:
            form = SignUpForm()
        return render(request, 'signup_login/signup.html', {'form': form})
    else:
        return HttpResponseRedirect('/exam_homepage/')


def user_login(request):
    # Get method
    if not request.user.is_authenticated:  # if user is logged in then block user from login from url
        log = AuthenticationForm()

        if request.method == 'POST':
            log = AuthenticationForm(request=request, data=request.POST)
            if log.is_valid():
                uname = log.cleaned_data['username']
                upass = log.cleaned_data['password']

                user = authenticate(request, username=uname, password=upass)

                if user is not None:
                    login(request, user)
                    if request.user.is_superuser:
                        return redirect('adminhome')

                    elif request.user.is_client:
                        return redirect('clienthome')

                    return HttpResponseRedirect('homepage/')

        return render(request, 'signup_login/login.html', {'log': log})
    else:
        return HttpResponseRedirect('homepage/')


def user_logout(request):
    logout(request)
    return redirect('/')


def user_changepass(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(user=request.user)
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # to update session
                update_session_auth_hash(request, form.user)

                return HttpResponseRedirect('/exam_homepage/')
        return render(request, 'signup_login/changepass.html', {'form': form})

    else:
        return HttpResponseRedirect('/login/')
