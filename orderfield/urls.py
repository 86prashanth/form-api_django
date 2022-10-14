from django.urls import path
from .views import *

urlpatterns=[
    path('',hey,name='home'),
]