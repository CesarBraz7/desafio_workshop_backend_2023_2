from django.shortcuts import render
from rest_framework import generics
from .models import Jogador, Nome
from .serializers import JogadorSerializer, NomeSerializer

#CRUD = class Jogador()
class JogadorListCreate(generics.ListCreateAPIView):#classe que permite a criação de uma instancia no banco de dados
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    
class JogadorRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):#classe que permite a leitura, a mudança e o delete de uma instancia no banco de dados
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

#CRUD = class Nome()
class NomeListCreate(generics.ListCreateAPIView):#classe que permite a criação de uma instancia no banco de dados
    queryset = Nome.objects.all()
    serializer_class = NomeSerializer

class NomeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView): #classe que permite a leitura, a mudança e o delete de uma instancia no banco de dados
    queryset = Nome.objects.all()
    serializer_class = NomeSerializer