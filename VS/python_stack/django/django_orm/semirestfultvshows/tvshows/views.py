from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'tvshows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):  
    errors = Show.objects.basic_validator(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/tvshows/new')

    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/tvshows/')

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    to_update = Show.objects.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/tvshows/')

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    # NOTE: Delete one show!
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/tvshows')