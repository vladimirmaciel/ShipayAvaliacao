u = Users.objects.select_related('role').only(
    "name", "email", 'role__description')

print(u.query)


p = Restaurant.objects.select_related(
    'best_pizza').prefetch_related('best_pizza__toppings')
>> > print(p.query)

u = Users.objects.prefetch_related('description__descricao')

---------------------------------------------------------------------
questao: 1
SELECT "saf_users"."name",
"saf_users"."email",
"saf_roles"."description",
"saf_claims"."descricao"
FROM "saf_users"
INNER JOIN "saf_roles" ON("saf_users"."role_id"="saf_roles"."id")
LEFT OUTER JOIN "saf_users_description" ON("saf_users"."id"="saf_users_description"."users_id")
LEFT OUTER JOIN "saf_claims" ON("saf_users_description"."claims_id"="saf_claims"."id")

------------------------------------------------------------------------------------------------
questão 2:
    from saf.models import *
    Saf.objects.all.values('description', 'saf__roles', 'saf__claims')
    
    resp_u = Users.objects.values(
        "name", "email", "role__description", "description__descricao")
    print(resp_u.values())

    ------------------------------------------------------------------------------------------------
    3. - Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar, construa uma API REST que irá listar o papel de um usuário pelo “Id” (role_id).

    - Instalando o Django Rest Framework.
    -------------------------------------------------------------------------------------------------
    4 - 4. - Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar, construa uma API REST que irá criar um usuário. Os campos obrigatórios serão nome, e-mail e papel do usuário. A senha será um campo opcional, caso o usuário não informe uma senha o serviço da API deverá gerar essa senha automaticamente.

    Foi utilizado o serializer para validar os campos necessários
    --------------------------------------------------------------------------------------------------
    questao 6: dentro do projeto core existe tem o arquivo settings onde a várivel
    WALLET_X_TOKEN_MAX_AGE deve receber um valor
    exemplo: WALLET_X_TOKEN_MAX_AGE = 10
