# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login


# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy

from photos.forms import PhotoForm
from photos.models import Photo
from users.forms import LoginForm


def login(request):
    error_messages=[]
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('usr')
            password=form.cleaned_data.get('pwd')
            user=authenticate(username=username,password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request,user)
                    url=request.GET.get('next','photos_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
    else:
        form = LoginForm()

    context={
        'errors':error_messages,
        'login_form':form
    }
    return render(request,'users/login.html',context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('photos_home')

@login_required()
def create(request):
    """
    Muestra un formlario para crear una foto y la crea si la peticion es POST
    :param request: HttpRequest
    :return:HttpResponse
    """
    success_message=''
    if request.method=='GET':
        form=PhotoForm()
    else:
        photo_with_owner=Photo()
        photo_with_owner.owner=request.user #Asigno como usuario de la foto, el usuario autenticado
        form = PhotoForm(request.POST,instance=photo_with_owner)
        if form.is_valid():
            new_photo=form.save()
            form = PhotoForm()
            success_message='Guardado con éxito  '
            success_message +='<a href="{}">'.format(reverse_lazy('photo_detail',args=[new_photo.pk]))
            success_message +='Ver foto'
            success_message +='</a>'
    context={
        'form':form,
        'success_message':success_message
    }
    return render(request,'photos/new_photo.html',context)
