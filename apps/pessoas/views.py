from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
   """
    queryset = Pessoa.objects.all().order_by('-criado_em')
    serializer_class = PessoaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        self.request.data['usuario'] = self.request.user.id
        request.data._mutable = False
        return super(PessoaViewSet, self).create(request, *args, **kwargs)
