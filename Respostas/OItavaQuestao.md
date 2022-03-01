 ## 8.   Qual ou quais Padrões de Projeto/Design Patterns você utilizaria para normalizar serviços de terceiros (tornar múltiplas interfaces de diferentes fornecedores uniforme), por exemplo serviços de disparos de e-mails, ou então disparos de SMS. ATENÇÃO: Não é necessário implementar o Design Pattern, basta descrever qual você utilizaria e por quais motivos optou pelo mesmo.

> Para atender a necessidade de deseparos de e-mail e mensagem, seria utilizado o framework **Nameko**, conforme a documentação oficial. 
> Ele vem com suporte para : 
RPC sobre AMQP
Eventos assíncronos (pub-sub) sobre AMQP
HTTP GET e POST simples
RPC e assinaturas do Websocket (experimental)
O que atenderia a necessidade. 

### exemplo de código para implementação 

```
import yagmail
from nameko.rpc import rpc, RpcProxy


class Mail(object):
    name = "mail"

    @rpc
    def send(self, to, subject, contents):
        yag = yagmail.SMTP('myname@gmail.com', 'mypassword')
        # read the above credentials from a safe place.
        # Tip: take a look at Dynaconf setting module
        yag.send(to=to.encode('utf-8'),
                 subject=subject.encode('utf-8'),
                 contents=[contents.encode('utf-8')])


class Compute(object):
    name = "compute"
    mail = RpcProxy('mail')

    @rpc
    def compute(self, operation, value, other, email):
        operations = {'sum': lambda x, y: int(x) + int(y),
                      'mul': lambda x, y: int(x) * int(y),
                      'div': lambda x, y: int(x) / int(y),
                      'sub': lambda x, y: int(x) - int(y)}
        try:
            result = operations[operation](value, other)
        except Exception as e:
            self.mail.send.async(email, "An error occurred", str(e))
            raise
        else:
            self.mail.send.async(
                email,
                "Your operation is complete!",
                "The result is: %s" % result
            )
            return result

```



