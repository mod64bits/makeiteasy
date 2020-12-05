from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Telefone
from .serializers import TelefoneSerializer


class TelefonesViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
   """
    queryset = Telefone.objects.all().order_by('-criado_em')
    serializer_class = TelefoneSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

