5 . 
 # Crie uma documentação que explique como executar seu projeto em ambiente local e também como deverá ser realizado o ‘deploy’ em ambiente produtivo.

## Instalação
Aruqivos necessários para instalar e rodar o ambiente na maquina local

## 
Crie a máquina virtal na pasta do projeto:
```
python -m venv venv

```

Ative a máquina virtual: Crie a máquina virtual
* Windows:
```
.\venv\Scripts\activate
```
* Linux:
```
source env/bin/activate
```

Instale as dependências
```
pip install -r requirements.txt
```

Desative a máquina virtual: 
```
deactivate
```

```

### Banco de Dados

Para usar o sistema é necessário configurar as base de dados do E-OUV e do E-SIC.

1. O banco utilizado foi o PostgreSql, baixe o banco conforme o sistema operacional utilizado crie o usuário e senha para acesso, modificar o o arquivo settings.py;

### Credenciais
1. Crie um superusuário


python .\manage.py createsuperuser
```

## Para coloca o ambiente em produção : 
###  Para fazer o deploy em um ambiente em produção a sugestão seria utizar a plataforma heroku  para hospedando a aplicação, utilizar o github para hospedar o código-fonte e como controlador de versão utilizando o git.
### Jenkins seria utilizado para automatizar a parte de desenvolvimento, facilitando a integração contínua
