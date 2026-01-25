'''
Crie um programa que tenha uma funçao chamada voto()
que vai receber como parametro o ano de nascimento de
uma pessoa, retornando um valor Negado, Opcional ou Obrigatorio
nas eleiçoes
'''

def voto(ano):
    from datetime import date #declarar bibiotecas dentro da funçao
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'

print(voto(2000))