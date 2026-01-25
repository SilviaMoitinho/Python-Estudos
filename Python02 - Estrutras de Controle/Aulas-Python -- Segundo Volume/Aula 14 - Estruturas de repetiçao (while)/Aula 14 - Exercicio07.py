''' 
Escreva um programa que leia um numero n inteiro qualquer
e mostre na tela os n primeiros elementos de uma sequencia de Fibonachi
'''

print('Sequencia de FIBONACHI')
cont = 0
a = 0
b = 1
n = int(input('Quantos elementos da fibonachi voce quer ver?'))
print('{}'.format(a), end='')
print(' -- ', end='')
print('{}'.format(b), end='')
if n > 2:
    while cont != n-2:
        cont += 1
        c = a + b
        print(' -- ', end='')
        print('{}'.format(c), end='')
        a = b
        b = c