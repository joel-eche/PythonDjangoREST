
from rest_framework import serializers
# -*- coding:utf-8 -*-
from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields = '__all__'
        read_only_fields=('owner',)

class PhotoListSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        fields = ('id','name','url')
