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
            'all_quotes': Quotes.objects.all(),
        }
    return render(request, 'dashboard.html', context)

def create_quote(request):
    if request.method == "GET":
        return redirect('/')
    errors = Quotes.objects.quote_validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        # return redirect('/success')
    else:
        user = User.objects.get(id=request.session["user_id"])
        quote = Quotes.objects.create(
            author = request.POST['author'],
            quote = request.POST['quote'],
            creator = user
        )
        # return redirect('/success')
    return redirect('/success')

def users_quote(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': User.objects.get(id=request.session["user_id"]),
        'all_quotes': Quotes.objects.all(),
    }
    return render(request, 'quotes.html', context)

def edit(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.user_validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        user = User.objects.edit(request.POST)
        messages.success(request, "You have successfully Updated!")
        return redirect('/success')

def delete(request, id):
    quotes = Quotes.objects.get(id=id)
    quotes.delete()
    return redirect('/success')

def like(request, id):
    quotes = Quotes.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])
    # quotes.liked_by.add(user)
    user.liked_quotes.add(quotes)
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def back(request):
    return redirect('/success')