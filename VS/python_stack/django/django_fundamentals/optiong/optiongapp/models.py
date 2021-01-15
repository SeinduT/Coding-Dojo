from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import re
import bcrypt

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def user_validate(self, form):
        errors = {}
        if len(form['first_name']) < 4:
            errors['first_name'] = 'First Name must be at least 4 characters'

        if len(form['last_name']) < 4:
            errors['last_name'] = 'Last Name must be at least 4 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email already in use"

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if form['password'] != form['confirmpw']:
            errors['confirmpw'] = 'Passwords do not match'
        
        return errors
    
    def authenticate(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if not check:
            errors['email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), check[0].password.encode()):
                errors['email'] = "Email and password do not match."
        return errors


    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw,
        )
        
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class QuoteManager(models.Manager):
    def quote_validate(self, form):
        errors = {}
        if len(form['author']) < 3:
            errors['author'] = 'Author Name must be at least 3 characters' 
        if len(form['quote']) < 10:
            errors['quote'] = 'Quote must be at least 10 characters'
        return errors


class Quotes(models.Model):
    author = models.CharField(max_length=45)
    quote = models.TextField(max_length=255)
    creator = models.ForeignKey(User, related_name="has_created_quotes", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_quotes')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = QuoteManager()
    