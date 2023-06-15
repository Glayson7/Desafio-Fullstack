from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from register.views import ClienteViewSet, ContatoViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet)

clientes_router = NestedSimpleRouter(router, r"clientes", lookup="cliente")
clientes_router.register(
    r"contatos", ContatoViewSet, basename="cliente-contatos"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(clientes_router.urls)),
]
