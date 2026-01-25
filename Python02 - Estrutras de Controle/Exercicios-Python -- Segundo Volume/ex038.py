'''
Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Nao existe valor maior, os dois sao iguais
'''

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O PRIMEIRO numero é maior')
elif n2 > n1:
    print('O SEGUNDO numero é maior')
else:
    print('Os dois valores sao IGUAIS')