from django.http import HttpResponse
from django.shortcuts import render


def for_about(request):
    return render(request,'about.html', context={
        "name": "Kwaku", "age": 28
    })



def home(request):
    return render(request,'home.html')


