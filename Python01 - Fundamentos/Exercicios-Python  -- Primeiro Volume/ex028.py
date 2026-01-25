'''
Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 a 5
e peça para o usuario tentar descobrir qual foi o numero escohido pelo computador.
O programa devera escrever na tela se o usario venceu ou perdeu
'''

from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('Computador ganhou! Eu pensei no numero {} e nao no {}'.format(computador, jogador))