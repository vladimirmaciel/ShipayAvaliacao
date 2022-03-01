6 .   Nossos analistas de qualidade reportaram uma falha que só acontece em ambientes diferentes do local/desenvolvimento, os engenheiros responsáveis pelo ambiente de Homologação já descartaram problemas de infra-estrutura, temos que levantar o que está acontecendo.

Ao executar o comando para listar os logs (no stdio) do Pod de Jobs, capturei o seguinte registro de log:

> Analisando o arquivo de log abaixo 
> foi verificar que faltou declara uma váriavel 
> WALLET_X_TOKEN_MAX_AGE dentro do arquivo settings.py 
> poderia ser resolvido seguindo o exemplo: 
> 
'''
exemplo: WALLET_X_TOKEN_MAX_AGE = 10
'''

```
[2020-07-06 20:24:49,781: INFO/ForkPoolWorker-2] [expire_orders] - Finishing job…

[2020-07-06 20:34:49,721: INFO/ForkPoolWorker-1] [renew_wallet_x_access_tokens] Starting task that renew Access Tokens from Wallet X about to expire

[2020-07-06 20:34:49,723: ERROR/ForkPoolWorker-1] Task tasks.wallet_oauth.renew_wallet_x_access_tokens[ee561a2e-e837-4d98-b771-07f4e2b5ec70] raised unexpected: AttributeError("module 'core.settings' has no attribute ‘WALLET_X_TOKEN_MAX_AGE'") Traceback (most recent call last): File "/usr/local/lib/python3.7/site-packages/celery/app/trace.py", line 385, in trace_task R = retval = fun(args, kwargs) File "/usr/local/lib/python3.7/site-packages/celery/app/trace.py", line 650, in protected_call return self.run(args, kwargs) File "/opt/worker/src/tasks/wallet_oauth.py", line 15, in renew_wallet_x_access_tokens expire_at = now - settings.WALLET_X_TOKEN_MAX_AGE AttributeError: module 'core.settings' has no attribute ‘WALLET_X_TOKEN_MAX_AGE'

[2020-07-06 20:34:49,799: INFO/ForkPoolWorker-2] [expire_orders] - Starting job…

[2020-07-66 20:34:49,801: INFO/ForkPoolWorker-2] [expire_orders] - Filtering pending operations older than 10 minutes ago.
```