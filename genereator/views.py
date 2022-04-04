from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):

    return render(request, 'generator/home.html') 

def password(request):

    characters = list('abcdefghilmnophijklmnopqrstuywxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):  
        characters.extend(list('!@#$%^&*'))
   
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
#  select qilib tanlagan raqamni ol diyapmiz va 12 deb 12 talik parol qil diyapmiz default holatida

    length = int(request.GET.get('length',12))

    parol = ''
    for x in range(length):
        parol += random.choice(characters)

    return render(request, 'generator/password.html',{'password': parol})


def info(request):

    return render(request, 'generator/info.html')

