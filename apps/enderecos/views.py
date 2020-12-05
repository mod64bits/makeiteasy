from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
   """
    queryset = Endereco.objects.all().order_by('-criado_em')
    serializer_class = EnderecoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)



