'''
Faça um programa que leia um numero inteiro
e diga se ele é ou nao um numero primo
'''
from math import sqrt

primo = ''
n = int(input('Digite um numero: '))

if n > 1 and (n % 2 == 1):
    raiz = sqrt(n)
    raiz_int = int(sqrt(n))
    for c in range(2, raiz_int+1):
        resultado = n % c
        if resultado == 0:
            primo = 'NAO'
            print('o numero {} nao é primo'.format(n))
            break
    if primo == '':
        print('O numero {} é primo'.format(n))
elif n == 2:
    print('O numero {} é o unico numero par que é primo'.format(n))
elif (n % 2 == 0):
    print('Numeros pares nao podem ser primos, com excessao do 2')