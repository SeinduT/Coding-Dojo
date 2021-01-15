from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, form):
        errors = {}
        if len(form['title']) < 2:
            errors['title'] = "Show title should be at least 2 characters"
        if len(form['network']) < 3:
            errors['network'] = "Network name should be at least 3 characters"
        if len(form['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"       
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()    # add this line!

