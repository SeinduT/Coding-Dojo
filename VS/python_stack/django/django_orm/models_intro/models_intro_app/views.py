from django.shortcuts import render
from .models import Dragon

# Create your views here.
def index(request):
    context = {
        "all_dragons": Dragon.objects.all()
    }
    return render(request, 'index.html', context)
