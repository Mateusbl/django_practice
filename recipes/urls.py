
from django.urls import path

from recipes.views import home, contato, sobre

urlpatterns = [
    path('contato/', contato),
    path('', home),
    path('sobre/', sobre),]
