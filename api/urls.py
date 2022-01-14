from django.urls import path
from django.conf.urls import include
from .views import NewsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]