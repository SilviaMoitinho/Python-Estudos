'''
Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 a 5
e peça para o usuario tentar descobrir qual foi o numero escohido pelo computador.
O programa devera escrever na tela se o usario venceu ou perdeu
'''
import random
from time import sleep
n = random.randint(0,5) #Faz o computador 'pensar'
print('Pensei em um numero de 0 a 5! Tenta adivinhar qual foi!')
advinha = int(input(': ')) #Jogador tenta adivinhar
print('PENSANDO...')
sleep(2)
if advinha == n:
    print('PARABENS! Esse foi o numero que pensei!')
else:
    print('Errou! Eu pensei no numero {}'.format(n))