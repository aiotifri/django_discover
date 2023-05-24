from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ml.utils import generate_blagues


def index(request):
    return render(request,"home.html")


def generate_blague(request):
    output=generate_blagues("fais moi rire")
    return render(request,"generate_blague.html",context={"output":output })