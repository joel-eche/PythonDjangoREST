# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer

from rest_framework.renderers import JSONRenderer

class UserListAPI(APIView):
    def get(self, request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        serialized_users=serializer.data                #lista de diccionarios
        return Response(serialized_users)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):
    def get(self,request,pk):
        user=get_object_or_404(User,pk=pk)#(Modelo sobre el que tiene que buscar, criterio de búsqueda,
        serializer=UserSerializer(user)
        return Response(serializer.data)

    def put(self,request,pk):
        user = get_object_or_404(User, pk=pk)
        serializer=UserSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    