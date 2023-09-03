from django.db import models

class Nome(models.Model):
    nome = models.CharField(max_length=50) #nome do jogador, que esta sendo referenciado na class Jogador(), na variavel jogador
    
    def __str__(self):
        return self.nome


class Jogador(models.Model):
    id = models.AutoField(primary_key=True) #primary key, que vai ser usada para visualizar os jogadores no banco de dados
    jogador = models.ForeignKey(#classe que permite que uma tabela seja referenciada em outra
        Nome,
        max_length = 20,
        on_delete = models.CASCADE
    )
    #variavel que permite a escolha dos valores na lista
    choices_time = [ #o primeiro valor entra no banco de dados, o segundo aparece para o usuario
        ('SAO PAULO', 'são paulo'),
        ('PALMEIRAS', 'palmeiras'),
        ('FLAMENGO', 'flamengo'),
        ('SANTOS', 'santos'),
        ('SANTA CRUZ', 'santa cruz'),
        ('BOTAFOGO', 'botafogo'),
        ('FLUMINENSE', 'fluminense'),
        ('VASCO', 'vasco'),
        ('SPORT', 'sport'),
    ]
    time = models.CharField(choices = choices_time, max_length=50) #o choices= permite que  escolhamos alguns dos valores da lista choices_time
    gols = models.IntegerField()