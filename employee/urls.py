from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('findByEmail', views.find_by_email),
    path('getAll', views.get_all),
    path('getById', views.get_by_id),
    path('update', views.update),
    path('delete', views.delete),
]
