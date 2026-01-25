'''
Crie um programa que leia o ano de nascimento 
de 7 pessoas. No final mostre quantas pessoas 
ainda nao atingiram a maioridade.
'''

from datetime import date

menor = 0
maioridade = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Digite {}° ano de nascimento: '.format(c)))
    idade = atual - ano
    if idade < 18:
        menor += 1
    else:
        maioridade += 1

print('No total {} pessoas ainda nao atingiram a maioridade'.format(menor))