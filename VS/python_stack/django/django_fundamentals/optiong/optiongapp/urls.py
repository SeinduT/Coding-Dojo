from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('success/<int:id>', views.edit),
    path('user/<int:id>', views.users_quote),
    path('back', views.back),
    path('quotes/create', views.create_quote),
    path('likes/<int:id>', views.like),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit)

]