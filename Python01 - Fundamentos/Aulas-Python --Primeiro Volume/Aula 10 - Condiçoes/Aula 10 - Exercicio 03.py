'''
Crie um programa que leia um numero inteiro e mostre na tela
se ele é par ou impar
'''

n = int(input('Digite um numero: '))
c = n % 2
if c == 0:
    print('O numero {} é par!'.format(n))
else:
    print('O numero {} é impar!'.format(n))