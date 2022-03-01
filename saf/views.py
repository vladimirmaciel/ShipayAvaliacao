from rest_framework import viewsets, generics
from saf.models import Users, Roles, Claims
from saf.serializer import UsuerSerializer, RoleSerializer, ClaimsSerializer, ListaPapelUsuarioSerializer


class UsersviewSet(viewsets.ModelViewSet):
    """ Exibir  id , name,  description"""

    queryset = Users.objects.all()

    serializer_class = UsuerSerializer


class RolesviewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()

    # UsuerSerializer  classe responsável por serializar os usuarios
    serializer_class = RoleSerializer


class ClaimviewSet(viewsets.ModelViewSet):
    queryset = Claims.objects.all()

    # UsuerSerializer  classe responsável por serializar os usuarios
    serializer_class = ClaimsSerializer


class ListaPapelUsuarioviewSet(viewsets.ModelViewSet):
    """Listando o Pepel de um determinado usuário"""

    queryset = Users.objects.all()

    serializer_class = ListaPapelUsuarioSerializer
