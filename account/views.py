from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from account.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status as http_status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate




@api_view(['POST'])
def sign_up(request):
    data = request.data
    photo = data['photo']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    username = data['username']
    password = data['password']
    if User.objects.filter(username=username).exists():
        return Response('User already exists', status=http_status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response('Email already exists', status=http_status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        photo=photo,
        username=username,
        password=password
    )
    token, created = Token.objects.get_or_create(user=user)
    context = {
        'Message': 'Thank you for registering',
        'token': token.key,
    }
    return Response(context, status=http_status.HTTP_200_OK)

@api_view(['POST'])
def sign_in(request):
    data = request.data
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.get_or_create(user=user)[0]
        return Response({'token': token.key}, status=http_status.HTTP_200_OK)
    else:
        return Response('Invalid credentials', status=http_status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request):
    data = request.data
    user = request.user
    if user.is_authenticated:
        first_name = data['first_name']
        last_name = data['last_name']
        photo = data['photo']
        email = data['email']
        username = data['username']
        password = data['password']
        if first_name: user.first_name = first_name
        if last_name: user.last_name = last_name
        if photo: user.photo = photo
        if email: user.email = email
        if username: user.username = username
        if password: user.set_password(password)
        if User.objects.filter(username=username).exists():
            return Response('User already exists', status=http_status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response('Email already exists', status=http_status.HTTP_400_BAD_REQUEST)
        else:
            user.save()
            context = {
                'Message': 'Uptade profile!',
            }
            return Response(context, status=http_status.HTTP_200_OK)












