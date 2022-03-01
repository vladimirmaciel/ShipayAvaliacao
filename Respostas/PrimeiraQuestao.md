# __Shipay Back-end Challenge__
**Shipay Back-end Challenge**


1 .  Tomando como base a estrutura do banco de dados fornecida (conforme diagrama [ER_diagram.png] e/ou script DDL [1_create_database_ddl.sql], disponibilizados no repositório do github): Construa uma consulta SQL que retorne o nome, e-mail, a descrição do papel e as descrições das permissões/claims que um usuário possui.

> Conform foi solicitado na 
>  questão, baseado do diagrama 
>  **ER** 

```
SELECT "saf_users"."name",
       "saf_users"."email",
       "saf_roles"."description",
       "saf_claims"."descricao"
FROM "saf_users"
INNER JOIN "saf_roles" ON ("saf_users"."role_id" = "saf_roles"."id")
LEFT OUTER JOIN "saf_users_description" ON ("saf_users"."id" = "saf_users_description"."users_id")
LEFT OUTER JOIN "saf_claims" ON ("saf_users_description"."claims_id" = "saf_claims"."id")
```


