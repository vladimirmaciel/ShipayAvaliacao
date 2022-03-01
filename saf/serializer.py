from rest_framework import serializers
from saf.models import Users, Roles, Claims
from saf.validators import *

from random import choice
import string

#  Serializer seria como filtro dos dados que pretendo disponibilizar para Api


class ClaimsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Claims
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ['id', 'description']
        # fields = '__all__'


class UsuerSerializer(serializers.ModelSerializer):
    # retornar a funcao de determinado usuario
    # role = serializers.ReadOnlyField(source='role.description')

    class Meta:
        model = Users
        fields = '__all__'

    def validate(self, data):
        if not nome_valido(data['name']):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo"})
        if gerar_password(data['password']):
            
            Users.data['password'].save()
        return data
 


class ListaPapelUsuarioSerializer(serializers.ModelSerializer):
    # retornar a funcao de determinado usuario
    role = serializers.ReadOnlyField(source='role.description')

    class Meta:
        model = Users
        fields = ['id',  'name', 'role', ]
