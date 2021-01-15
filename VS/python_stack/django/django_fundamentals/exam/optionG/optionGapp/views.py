from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
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
            'all_quotes': Quotes.objects.all()
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

def users_quote(request, user_id):
    quotes = Quotes.objects.all()
    context = {
        'author': Quotes.objects.author,
        'quotes': Quotes.objects.quote,
        'creator': Quotes.User.name,
        'liked_by': Quotes.objects.liked_by
    }
    return render(request, 'quotes.html', context)

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    errors = User.objects.user_validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        user = User.objects.edit(request.POST)
        messages.success(request, "You have successfully Updated!")
        return redirect('/success')

def delete(request, quote_id):
    quote = Quotes.objects.get(id=quote_id)
    quote.delete()

def like(request, quote_id):
    user = User.objects.get(id=request.session["user_id"])
    quote = Quotes.objects.get(id=quote_id)
    user.liked_quotes.add(quote)

def logout(request):
    request.session.clear()
    return redirect('/')
