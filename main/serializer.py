from rest_framework import serializers

from main.models import *

from account.serializeruser import UserSerializer


class ProcessModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['name', 'description']

class ContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['image', 'name']


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class RecipeModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    class Meta:
        model = Recipe
        fields = ['category', 'image', 'name']

class RecipeDetailSerializer(RecipeModelSerializer):
    processes = ProcessModelSerializer(many=True)
    contents = ContentModelSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['category', 'image', 'name', 'processes', 'contents']

class FavoriteRecipeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteRecipe
        fields = ['recipe']
        depth = 2

class CategoryIdFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['category', 'image', 'name']
        depth = 1


