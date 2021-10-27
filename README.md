# pewek-cnpj
API que viabiliza a consulta de informações por CNPJs

## Requisitos
Você precisa ter o Python3.8+ instalado junto com o pip
Você instalar todos as bibliotecas obrigatórias com o pip
```
sudo pip install requirements
```

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

## Executando sem docker


