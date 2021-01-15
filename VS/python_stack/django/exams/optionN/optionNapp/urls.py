from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('posts_thought', views.post_thought),
    path('posts/<int:id>', views.thought),
    path('addlike/<int:id>', views.add_like),
    path('removelike/<int:id>', views.unlike),
    path('delete/<int:id>', views.delete_post),
]