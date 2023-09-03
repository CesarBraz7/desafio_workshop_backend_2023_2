from django.urls import path
from .views import JogadorListCreate, JogadorRetrieveUpdateDelete, NomeListCreate, NomeRetrieveUpdateDelete

urlpatterns = [
    path('nome/', NomeListCreate.as_view(), name= "create-nome"), #url para criar o nome do jogador
    path('nome/<int:pk>/', NomeRetrieveUpdateDelete.as_view(), name = 'nome-details'),#url para editar o nome do jogador
    path('jogadores/', JogadorListCreate.as_view(), name= "jogadores"), #url para criar as instancias do jogador
    path('jogadores/<int:pk>/', JogadorRetrieveUpdateDelete.as_view(), name = 'artilheiros') #url para editar as instancias do jogador
]
