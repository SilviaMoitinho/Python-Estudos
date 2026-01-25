'''
Faça um programa que ajude um jogador da MegaSena
a criar palpites. O programa vai perguntar, quantos jogos
serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
jogos = [[]]
cont = 0
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
r = int(input('Quantos jogos voce quer que eu sorteie? '))
print('{:-^30}'.format(f' Sorteando {r} jogos '))
for c in range(1, r+1):
    for j in range(0,6):
        n = randint(1,60)
        if n not in jogos:
            jogos[cont].append(n)
    sleep(1)
    print(f'Jogo {c}: {sorted(jogos[cont])}')
    jogos.append([])
    cont += 1
print('{:-^30}'.format(' Boa Sorte '))