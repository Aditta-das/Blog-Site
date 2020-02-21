from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from .models import *

def signup(request):

    return render(request, 'signup.html')


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        count = User.objects.filter(username=username, password=password).count()

        if count > 0:
            request.session['is_logged'] = True
            request.session['user_id'] = User.objects.values('id').filter(username=username, password=password)[0]['id']
            print(id)
            return redirect('/')

        else:
            return redirect('signin')

    return render(request, 'signin.html')

def signout(request):
    del request.session['is_logged']

    return redirect('signin')

def new_register(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        obj = User(username=username, email=email, password=password)

        obj.save()
        return redirect('signin')
