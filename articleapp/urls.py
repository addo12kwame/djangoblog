from .views import articles_home
from django.urls import path
urlpatterns = [

    path('', articles_home)
]


