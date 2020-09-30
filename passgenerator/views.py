from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'passgenerator/home.html')

def password(request):
    characters = list('abcedfghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specchar'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length',10))
    password = ''
    for x in range(length):
        password += random.choice(characters)
    return render(request, 'passgenerator/password.html',{'password':password})

def aboutus(request):
    return render(request, 'passgenerator/aboutus.html')
