'''
Faça um programa que leia um numero qualquer e mostre o seu fatorial
'''

# Soluçao com modulo
from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# Soluçao com while
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))