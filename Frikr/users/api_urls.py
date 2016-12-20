from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

#APIRouter
router=DefaultRouter()
router.register(r'users',UserViewSet,base_name='user')

urlpatterns = [
    #API URLs
    url(r'1.0/',include(router.urls)), #incluyo las URLs de API
]
