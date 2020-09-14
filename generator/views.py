from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'B@2123sim'})


def about(request):
    # return HttpResponse("<H1>generator app generates new passwords for every refresh</H1>")
    return render(request, 'generator/about.html')


def password(request):
    the_password = ""
    characters = list()
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('lowercase'):
        characters.extend('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('@!#$%^&*')

    for x in range(length):
        the_password += random.choice(characters)

    # the_password = "Please select checkbox,So that secure password will be generated..."

    return render(request, 'generator/password.html', {'pwd': the_password})


def helpsec(request):
    return render(request, 'generator/helpsection.html')
