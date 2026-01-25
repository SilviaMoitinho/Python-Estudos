'''
Faça um programa que tenha uma lista chamada numeros e duas funçoes
chamadas sorteia() e somapar(). A primeira funçao vai sortear 5 numeros 
e vai colocalos dentro da lista e a segunda funçao vai mostrar a soma 
entre todos os valores pares sorteados pela funçao anterior.
'''

from random import randint

valores = []

def sorteia(num):
    print('-'*30)
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        num.append(randint(0,10))
        print(f'{num[c]} ', end='')
    print()

def somapar(n):
    par = 0
    print('-'*30)
    print(f'Somando os valores pares de {n}, ', end='')
    for c in range(0, len(n)):
        if n[c] % 2 == 0:
            par += n[c]
    print(f'temos {par}')
    print()
    

sorteia(valores)
somapar(valores)