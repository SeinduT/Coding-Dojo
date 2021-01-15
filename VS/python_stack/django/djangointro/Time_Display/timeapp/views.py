from django.shortcuts import render
from time import gmtime, strftime
import datetime

def showtime(request):
    context = {
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

# Create your views here.
