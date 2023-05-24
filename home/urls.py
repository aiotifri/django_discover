
from django.urls import path

from home.views import index, generate_blague

urlpatterns = [

    path("",index),
    path("gen",generate_blague)
]
