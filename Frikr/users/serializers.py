#-*- encoding:utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField() #Sólo lectura
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos de validated_data
        que contiene valores deserializados
        :param validated_data:Diccionario con datos de usuario
        :return:Objeto user
        """
        instance=User()
        return self.update(instance,validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de datos del diccionario
        validated_data que contiene valores deserializados
        :param instance: objeto User a actualizar
        :param validated_data: diccionario con nuevos valores para el User
        :return: objeto User actualizado
        """

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))  # Encripta la contraseña
        instance.save()
        return instance

    def validate_username(self,data):
        """
        Valida si existe un usuario con ese username
        """
        user=User.objects.filter(username=data)

        #Si estoy creando(no hay instancia)comprobar si hay usuarios con ese username
        if not self.instance and len(user)!=0:
            raise serializers.ValidationError(u'Ya existe un usuario con ese username ')

        #Si estoy actualizando(hay instancia), y cambiamos el username
        #(está cambiando el username) y existen usuarios registrados con el nuevo username
        elif self.instance and self.instance.username != data and len(user)!=0:
            raise serializers.ValidationError(u'Ya existe un usuario con ese username ')
        else:
            return data
