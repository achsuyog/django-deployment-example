from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Suyog'});

def add(request):
    name = request.POST['name']
    age = request.POST['age']
    #  res = num1+num2
    return render(request, 'result.html',{'name':name,'age':age})

