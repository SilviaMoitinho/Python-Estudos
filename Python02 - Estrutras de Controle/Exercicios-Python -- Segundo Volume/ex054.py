'''
Crie um programa que leia o ano de nascimento 
de 7 pessoas. No final mostre quantas pessoas 
ainda nao atingiram a maioridade.
'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivemos {} menores de idade'.format(totmenor))
