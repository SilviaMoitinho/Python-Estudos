'''
Faça um programa que tenha uma lista chamada numeros e duas funçoes
chamadas sorteia() e somapar(). A primeira funçao vai sortear 5 numeros 
e vai colocalos dentro da lista e a segunda funçao vai mostrar a soma 
entre todos os valores pares sorteados pela funçao anterior.
'''

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
