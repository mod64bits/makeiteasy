# Sistema Make It Easy

## Equipe:
> ### mod64bits (Marcio Oliveira D.) Email: mod64bits@gmail.com

> ### Raphael ()

> ## Instalação:

```
python3 -m venv venv
```
```
. venv/bin/activate
```

```
pip install -R requirements.txt
```
```
./manage.py makemigrations 
```
```
./manage.py migrate        
```

```
 ./manage.py createsuperuser
```
> #### Cadastre Email e Senha do admin:

> ### Desenvolvimento
>  docker-compose up  
> Crie o Banco de dados chamado easy
> ou edite as configurações de banco de dados em settings.py
 
> ## Endpoint

> "telefones": "http://127.0.0.1:8000/api/v1/telefones/"

> "enderecos": "http://127.0.0.1:8000/api/v1/enderecos/"

> "pessoas": "http://127.0.0.1:8000/api/v1/pessoas/"
 

> "users": "http://127.0.0.1:8000/api/v1/users/"
