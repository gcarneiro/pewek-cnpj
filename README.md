# pewek-cnpj
API que viabiliza a consulta de informações por CNPJs

## Requisitos
Você precisa ter o Python3.8+ instalado junto com o pip
Você instalar todos as bibliotecas obrigatórias com o pip
```
sudo pip install -r requirements.txt
```

## Como utilizar?
Basta fazer um acesso ao seu endereço no path cnpj/{cnpj}

Ex: http://localhost/cnpj/00000000000191

## Apontamento para banco de dados
Você precisará ter o banco de dados oferecido pela receita construído sob um banco mysql/mariadb. Você deverá criar um arquivo de configuração json, chamado de config.json no root do projeto.

```
{
    "host": "hostname",     
"port": "porta",     
"user": "usuario",     
"password": "senha", 
"database": "schema"
}
```

No projeto https://github.com/gcarneiro/open-data-cnpj-import temos o script que irá importar esse banco de dados direto da RF brasileira

## Executando a api

### Sem utilização de docker
Basta você navegar até o seu projeto e executa-lo como um script python, neste modelo ele irá expor a porta 5002 por padrão
```
python3 api.py
```

### Utilizando docker (recomendado)

Você precisa inicialmente buildar sua imagem docker
```
sudo docker build . -t pewek-cnpj-api
```

Após buildar sua imagem você precisa criar seu container
```
sudo docker run -d -p 5020:5020 --name=pewek-cnpj --restart=always pewek-cnpj-api:latest
```

Neste modo o docker irá expor a porta 5020


