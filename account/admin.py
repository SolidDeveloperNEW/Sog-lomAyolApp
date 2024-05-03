from django.contrib import admin
from account.models import User
from main.models import FavoriteRecipe

admin.site.register(User)
admin.site.register(FavoriteRecipe)
