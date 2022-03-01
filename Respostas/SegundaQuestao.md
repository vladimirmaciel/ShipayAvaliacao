2 .   Utilizando a mesma estrutura do banco de dados da questão anterior, rescreva a consulta anterior utilizando um ORM (Object Relational Mapping) de sua preferência utilizando a query language padrão do ORM adotado (ex.: Spring JOOQ, EEF LINQ, SQL Alchemy Expression Language, etc).

> Conform foi solicitado na 
>  questão, baseado do diagrama 
>  **ER** 

```
 Saf.objects.all.values('description', 'saf__roles', 'saf__claims')
    from saf.models import *

    resp_u = Users.objects.values(
        "name", "email", "role__description", "description__descricao")
    print(resp_u.values())
```