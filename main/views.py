from main.models import *
from account.models import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status as http_status
from account.serializeruser import *
from main.serializer import *
from account.permission import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['GET'])
def get_recipe(request):
    category_id = request.GET.get('category_id')
    if category_id:
        category = Category.objects.filter(id=category_id).first()
        if category:
            recipes = category.recipe_set.all()
            serializers = CategoryIdFilterSerializer(recipes, many=True)
            return Response(serializers.data, status=http_status.HTTP_200_OK)
        else:
            return Response('Category Not found', status=http_status.HTTP_404_NOT_FOUND)


    recipes = Recipe.objects.all().order_by('-id')
    serializer = RecipeModelSerializer(recipes, many=True)
    return Response(serializer.data, status=http_status.HTTP_200_OK)

@api_view(['GET'])
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    serializer = RecipeDetailSerializer(recipe)
    return Response(serializer.data, status=http_status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def favorite_recipe(request):
    data = request.data
    user = request.user
    recipe_id = request.data.get('recipe_id')

    if recipe_id:
        try:
            recipe = FavoriteRecipe.objects.get(user=user, recipe_id=recipe_id)
            return Response('Recipe is already a favorite', status=http_status.HTTP_200_OK)
        except FavoriteRecipe.DoesNotExist:
            favorite = FavoriteRecipe.objects.create(user=user, recipe_id=recipe_id)
            return Response('Recipe added to favorites', status=http_status.HTTP_200_OK)
    else:
        return Response('Recipe id not provided', status=http_status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_favorites(request):
    user = request.user
    recipe_id = request.GET.get('recipe_id')
    if recipe_id:
        favorites = FavoriteRecipe.objects.filter(user=user, recipe_id=recipe_id)
        if favorites.exists():
            serializers = FavoriteRecipeModelSerializer(favorites)
            return Response(serializers.data, status=http_status.HTTP_200_OK)
        else:
            return Response('Recipe not found', status=http_status.HTTP_404_NOT_FOUND)
    favorites = FavoriteRecipe.objects.filter(user=user)
    if favorites.exists():
        serializers = FavoriteRecipeModelSerializer(favorites, many=True)
        return Response(serializers.data, status=http_status.HTTP_200_OK)
    else:
        return Response('Favorites not found', status=http_status.HTTP_404_NOT_FOUND)







