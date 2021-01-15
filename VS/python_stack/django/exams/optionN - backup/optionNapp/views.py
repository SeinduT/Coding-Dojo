from django.shortcuts import render, redirect
from .models import User, Quotes
from django.contrib import messages
from django.db.models import Count
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.user_validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/success')

def login(request):
    errors = User.objects.authenticate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session["user_id"]),
            'all_thoughts': Post.objects.all(),
        }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def post_thought(request):
    Post.objects.create(thought=request.POST['mess'], poster=User.objects.get(id=request.session['id']))
    return redirect('/success')

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')

def delete_post(request, id):
    destroyed = Post.objects.get(id=id)
    destroyed.delete()
    return redirect('/success')
