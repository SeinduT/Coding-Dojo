from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('quotes', views.users_quote),
    path('quotes/create', views.create_quote),
    path('like', views.like),
    path('edit', views.edit)
]
