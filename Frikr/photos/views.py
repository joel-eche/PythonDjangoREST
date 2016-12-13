#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo, PUBLIC


def home(request):
    photos=Photo.objects.filter(visibility=PUBLIC).order_by('-created_at',)
    context={
        'photos_list':photos[:5]
    }
    return render(request,'photos/home.html',context)

def detail(request,pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    possible_photos = Photo.objects.filter(pk=pk).select_related('owner')
    photo=possible_photos[0] if len(possible_photos)>=1 else None

    if photo is not None:
        context={
            'photo':photo
        }
        return render(request,'photos/detail.html',context)
    else:
       return HttpResponseNotFound("No existe la foto wey u.u")#404 not found