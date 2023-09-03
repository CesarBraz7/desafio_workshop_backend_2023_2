# Tabela de jogadores
## API com CRUD
Essa API, feita com o Django Rest Framework, permite que jogadores de futebol sejam cadastrados no banco de dados PostgreSQL. Além disso, também permite que eles sejam editados e apagados.

### Comandos importantes

Comando para habilitar scripts no powershell

```ps1
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

Comandos para preparar as migrações no app

```ps1
python manage.py makemigrations
```

Comandos para realizar as migrações no app

```ps1
python manage.py migrate
```

Comandos para inicializar o servidor

```ps1
python manage.py runserver
```

### Como utilizar

- Ao inicializar o servidor, será disponibilizado a porta do servidor. Colocando o cursor em cima da porta, **Ctrl+Click**.

- No URL, colocando a path `nome/`, conseguimos cadastrar o nome de um jogador. Após o cadastro, recebemos um ID. e colocando a path `nome/{id-do-jogador}`, podemos editar seu nome ou apagá-lo do banco de dados.

- Na path `jogadores/`, podemos escolher o time e o nome pré-cadastrados, e também podemos dizer a quantidade de gols que ele fez. Nos será retornado o ID do cadastro, o time do jogador, a quantidade de gols e o ID do jogador cadastrado.

- Da mesma forma, acessando `jogadores/{id-do-cadastro}`, pode ser feito a edição e a remoção do seu time,  a quantidade de gols, e o jogador cadastrado.