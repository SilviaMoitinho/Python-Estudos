'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues.
OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
'''

print('┏━━━━━━━━━━━━━━━━━━━━━━━━━┓')
print('     🪙   \033[34mBANCO PYT\033[m')
print('┗━━━━━━━━━━━━━━━━━━━━━━━━━┛')

cont50 = cont20 = cont10 = cont1 = 0

n = int(input('Quantidade que deseja sacar: R$'))

while True:
    if n == 0:
        break
    elif n >= 50:
        n -= 50
        cont50 += 1
    elif n < 50 and n >= 20:
        n -= 20
        cont20 += 1
    elif n < 20 and n >= 10:
        n -= 10
        cont10 += 1
    elif n < 10 and n >= 1:
        n -= 1
        cont1 += 1
print('-'*30)
print('')
if cont50 > 0:
    print(f' cedulas de 50 : \033[33m{cont50}\033[m')
if cont20 > 0:
    print(f' cedulas de 20 : \033[33m{cont20}\033[m')
if cont10 > 0:
    print(f' cedulas de 10 : \033[31m{cont10}\033[m')
if cont1 > 0:
    print(f' cedulas de 1 : \033[32m{cont1}\033[m')
print('')
print('Obrigado por utilizar nossos serviços! Volte sempre!')
print('\033[34mBANCO PYT\033[m')