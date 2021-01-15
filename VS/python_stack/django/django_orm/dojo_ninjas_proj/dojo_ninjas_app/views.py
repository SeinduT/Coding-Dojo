from django.shortcuts import render, redirect
from .models import Dojo
from .models import Ninja

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def create(request):
