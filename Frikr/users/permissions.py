# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Define si el ususario autenticado en request.user
        tiene permiso para realizar la acción (GET,POST,PUT
        o DELETE)
        """

        #Si quiere crear un usuario, sea quien sea, debe poder crearlo

        from users.api import UserDetailAPI
        if request.method=='POST':
            return True
        #Si no, si es superuser puede hacer lo que quiera
        elif request.user.is_superuser:
            return True
        #Sino, si no es POST (es GET,PUT o DELETE), el usuario no es superuser
        #y la petición va a la vista de detalle, entonces lo permitimos
        #para tomar la decisión en el método has_object_permission
        elif isinstance(view,UserDetailAPI):
            return True
        #GET a /api/1.0/users/
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
            Define si el ususario autenticado en request.user
            tiene permiso para realizar la acción (GET,POST,PUT
            o DELETE) sobre el objeto obj
        """
        #Si es superadmin, o el usuario autenticado intenta
        #hacer GET,PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user==obj