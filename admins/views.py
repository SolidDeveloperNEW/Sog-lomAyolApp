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

@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdmin])
def recipe_update(request):
    data = request.data
    user = request.user
    recipe = Recipe.objects.all()
    if request.method == "POST":
        recipe = recipe[0]
        category_id = data['category_id']
        image = data['image']
        name = data['name']
        if category_id: recipe.category_id = category_id
        if image: recipe.image = image
        if name: recipe.name = name
        if Recipe.objects.filter(name=name).exists():
            return Response('Recipe already exists', status=http_status.HTTP_400_BAD_REQUEST)
        else:
            recipe.save()
            return Response('Recipe created', status=http_status.HTTP_201_CREATED)
    if request.method == "PUT":
        recipes = request.data.get('recipes_id')
        category_id = request.data.get('category_id')
        image = request.data.get('image')
        name = request.data.get('name')
        if recipes:
            if Recipe.objects.filter(id__in=recipe).exists():
                recipe = recipe[0]
                recipe.category_id = category_id
                recipe.name = name
                recipe.image = image
                recipe.save()
                return Response('Recipe updated', status=http_status.HTTP_200_OK)
            else:
                return Response('Recipe not found', status=http_status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        recipe_id = request.GET.get('recipe_id')
        if recipe_id:
            recipe = Recipe.objects.get(id=recipe_id)
            recipe.delete()
            return Response('Recipe deleted', status=http_status.HTTP_200_OK)
        else:
            return Response('Recipe not found', status=http_status.HTTP_404_NOT_FOUND)
    else:
        return Response('Method not allowed', status=http_status.HTTP_405_METHOD_NOT_ALLOWED)

