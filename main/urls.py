
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('auction_cars', views.HomeView,)

#app_name = "main"
urlpatterns = [
    path('', include(router.urls)),
]