from django.urls import path
from admins.views import *

urlpatterns = [
    path('admins/', recipe_update)
]