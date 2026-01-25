'''
Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Nao existe valor maior, os dois sao iguais
'''
from time import sleep
print('Comparando numeros!')
print('Digite dois numeros e o programa vai analisar qual é o maior.')
n1 = int(input('\033[34mPrimeiro\033[m numero -> '))
n2 = int(input('\033[33mSegundo\033[m numero -> '))
print('Aguarde, estou analisando os numeros ...')
sleep(2)
if n1 > n2:
    print('O \033[34mprimeiro\033[m valor é maior \033[34m({})\033[m'.format(n1))
elif n2 > n1:
    print('O \033[33msegundo\033[m valor é maior \033[33m({})\033[m'.format(n2))
elif n1 == n2:
    print('Nao existe valor maior, \033[32mos dois sao iguais.\033[m')