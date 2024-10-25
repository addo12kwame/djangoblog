from .views import articles_home,article_detail
from django.urls import path



app_name = "articles"


urlpatterns = [

    path('', articles_home, name='home'),
    path('<slug>/', article_detail, name='detail'),  # this name capturing group lets you get a second param (slug) on the view function
]


