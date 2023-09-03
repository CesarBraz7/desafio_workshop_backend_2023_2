from rest_framework import serializers
from .models import Jogador, Nome

#serializador das informações do jogador
class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ('__all__')

#serializador do nome do jogador
class NomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nome
        fields = ('__all__')