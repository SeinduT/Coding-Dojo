from django.shortcuts import render, redirect
from .models import Book
from .models import Author

# Create your views here.
def index(request):
    return render(request, 'index.html')