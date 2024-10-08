from django.shortcuts import render
from .models import Article

# Create your views here.


def articles_home(request):
    article =Article.objects.all().order_by('date')
    return render(request, 'articleapp/articles_home.html', context={'article':article})
