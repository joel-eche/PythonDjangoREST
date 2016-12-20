# -*- coding:utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotosQueryset

class PhotoViewSet(PhotosQueryset,ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photo_queryset(self.request)

    def get_serializer_class(self):
        if self.action=='list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto al
        usuario autenticado
        """
        serializer.save(owner=self)

class PhotoListAPI(PhotosQueryset,ListCreateAPIView):
    queryset=Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    #serializer_class = PhotoListSerializer
    def get_serializer_class(self):
        return PhotoSerializer if self.request.method=="POST" else PhotoListSerializer

    def get_queryset(self):
        return self.get_photo_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotoDetailAPI(PhotosQueryset,RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photo_queryset(self.request)
