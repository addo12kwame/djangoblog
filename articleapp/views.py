from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.


def articles_home(request):
    article =Article.objects.all().order_by('date')
    return render(request, 'articleapp/articles_home.html', context={'article':article})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request,"articleapp/detail.html", {'article': article })


