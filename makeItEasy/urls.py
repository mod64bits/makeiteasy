from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from apps.pessoas.views import PessoaViewSet
from apps.usuarios.views import UserViewSet
from apps.enderecos.views import EnderecoViewSet
from apps.telefones.views import TelefonesViewSet

router = routers.DefaultRouter()
router.register(r'telefones', TelefonesViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'pessoas', PessoaViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]
