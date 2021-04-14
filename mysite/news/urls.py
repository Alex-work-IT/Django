from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('admin', admin, name='admin'),
    path('create', create, name='create'),
]
