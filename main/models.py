from django.db import models
from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.id}'

class Process(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.id}'

class Content(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='contents/')

    def __str__(self):
        return f'{self.name} - {self.id}'

class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipe/')
    name = models.CharField(max_length=100)
    processes = models.ManyToManyField(Process)
    contents = models.ManyToManyField(Content)

    def __str__(self):
        return f'{self.name} - {self.id}'

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe.name} - {self.id}'
