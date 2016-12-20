"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet
from photos.views import DetailView, HomeView, CreateView,PhotoListView,UserPhotosView
from users.api import UserViewSet
from users.views import LoginView, LogoutView

#APIRouter
router=DefaultRouter()
router.register(r'api/1.0/photos',PhotoViewSet)
router.register(r'api/1.0/users',UserViewSet,base_name='user')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #Photos URLs
    url(r'^$',HomeView.as_view(), name='photos_home'),
    url(r'^my-photos/$',login_required(UserPhotosView.as_view()),name='photos_user'),
    url(r'^photos/$',PhotoListView.as_view(),name='photos_list'),
    url(r'^photos/(?P<pk>[0-9]+)/$',DetailView.as_view(),name='photo_detail'),
    url(r'^photos/new',CreateView.as_view(),name='photo_create'),

    #Users URLs
    url(r'^login$',LoginView.as_view(),name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    #API URLs
    url(r'',include(router.urls)), #incluyo las URLs de API
    #url(r'api/1.0/photos/$',PhotoListAPI.as_view(),name='photo_list_api'),
    #url(r'api/1.0/photos/(?P<pk>[0-9]+)/$',PhotoDetailAPI.as_view(),name='photo_detail_api'),
    #url(r'api/1.0/users/$',UserListAPI.as_view(),name='user_list_api'),
    #url(r'api/1.0/users/(?P<pk>[0-9]+)/$',UserDetailAPI.as_view(),name='user_detail_api'),
]
