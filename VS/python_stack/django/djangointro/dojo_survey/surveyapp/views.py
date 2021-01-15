from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment']
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')

# Create your views here.