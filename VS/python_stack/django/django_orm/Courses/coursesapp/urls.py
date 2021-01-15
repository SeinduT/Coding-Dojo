from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.index),
    path('courses/create', views.create),
    path('courses/<int:id>', views.comments),
    path('courses/<int:id>/comment', views.create_comment),
    path('courses/<int:id>/delete', views.delete)
]
