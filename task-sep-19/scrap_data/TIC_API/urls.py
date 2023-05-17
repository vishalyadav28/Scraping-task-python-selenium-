from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import TICViewset


router=DefaultRouter()

router.register('TIC_API',TICViewset,basename='TIC_API')
urlpatterns = [
    path('',include(router.urls)),
]