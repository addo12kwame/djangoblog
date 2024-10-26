from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

@login_required(login_url="accounts:login")
def articles_home(request):
    article =Article.objects.all().order_by('date')
    return render(request, 'articleapp/articles_home.html', context={'article':article})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request,"articleapp/detail.html", {'article': article })

@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == "POST":

        # if there is a file upload, you need to add a second argument 'request.FILES'
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:home")


    else:
        form = forms.CreateArticle()
    return render(request,"articleapp/article_create.html",{'form':form})



