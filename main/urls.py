from django.urls import path
from main.views import *

urlpatterns = [
    path('get-recipe/', get_recipe),
    path('get-recipe/<int:recipe_id>/', recipe_detail),
    path('favorite-recipe/', favorite_recipe),
    path('get-favorite/', get_favorites),

]