from django.urls import path

from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from speed.api import views as sv

router = DefaultRouter()
router.register(r"speed", sv.UserDataViewSet)
router.register(r"report", sv.ReportUserViewSet)

urlpatterns = [
    path("", include(router.urls))
]