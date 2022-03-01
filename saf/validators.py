import re
from random import choice
import string


def nome_valido(nome):
    return nome.isalpha()


def gerar_password(password):
    """Gera um password caso o campo esteja em branco)"""
    if password =="":

        tamanho = 5
        valores = string.ascii_lowercase
        password = ''
        for i in range(tamanho):
            password += choice(valores)
    return password

       
