from django.urls import path, include
from rest_framework.routers import DefaultRouter
from register.views import ClienteViewSet, ContatoViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'contatos', ContatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
