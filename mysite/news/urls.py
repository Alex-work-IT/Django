from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('admin', admin, name='admin'),
    path('create', create, name='create'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
