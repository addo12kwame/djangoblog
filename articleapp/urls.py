from .views import articles_home,article_detail,article_create
from django.urls import path



app_name = "articles"


urlpatterns = [

    path('', articles_home, name='home'),
    # this should come before the slug url because it will think create is a slug
    # it will think create is <slug>
    path('create/', article_create, name='create'),
    path('<slug>/', article_detail, name='detail'),  # this name capturing group lets you get a second param (slug) on the view function
]


