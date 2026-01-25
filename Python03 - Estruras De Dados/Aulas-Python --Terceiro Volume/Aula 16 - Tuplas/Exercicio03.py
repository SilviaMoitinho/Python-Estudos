'''
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
Depois disso, mostre a listagem de numeros gerados e tambem indique o
menor e o maior valor que estao na tupla
'''

from random import randint
tup = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = menor  = 0
print(' ★ '*10)
print('Os numeros sortados foram: ', end='')
print(f'\nO maior numero é {max(tup)}')
print(f'O menor numero é {min(tup)}')