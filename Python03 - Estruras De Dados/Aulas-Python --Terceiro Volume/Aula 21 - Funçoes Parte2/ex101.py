'''
Crie um programa que tenha uma funçao chamada voto()
que vai receber como parametro o ano de nascimento de
uma pessoa, retornando um valor Negado, Opcional ou Obrigatorio
nas eleiçoes
'''

from datetime import datetime

def voto(num):
    idade = datetime.now().year - num
    if idade < 18:
        return idade, ('Voto NEGADO.')
    elif idade >= 18 and idade < 65:
        return idade, ('Voto OBRIGATORIO')
    else:
        return idade, ('Voto OPCIONAL')


print('-'*30)
nasc = int(input('Em que ano voce nasceu? '))
print(f'Com {voto(nasc)[0]} anos: {voto(nasc)[1]}')
