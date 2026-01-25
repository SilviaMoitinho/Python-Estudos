'''
Crie um programa que leia um numero inteiro e mostre na tela
se ele é par ou impar
'''

numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))