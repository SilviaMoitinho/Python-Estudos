'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
Seu programa devera realizar a operaçao solicitada em casa caso
'''

from time import sleep

print('ﾟ･✻･ﾟ･✻･ﾟﾟ･✻･ﾟ･✻･ﾟﾟ･✻･ﾟ･✻･ﾟﾟ･✻･ﾟﾟ･✻･ﾟ･✻･ﾟﾟ･✻･ﾟ･✻･ﾟﾟ･✻･ﾟ･✻･ﾟﾟ･✻･ﾟ')
print('     Bem Vindo ao programa \033[35mContas com Python\033[m')
print('')
print('Para começar, por favor digite... ⤵ ')
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
menu = 0

while menu != 5:
    print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('            MENU')
    print('')
    print('  [1] \033[36mSomar\033[m')
    print('  [2] \033[32mMultiplicar\033[m')
    print('  [3] \033[33mMaior\033[m')
    print('  [4] \033[34mNovos numeros\033[m')
    print('  [5] \033[31mSair do Programa\033[m')
    print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    print('')
    menu = int(input('  -> '))
    if menu == 1:
        soma = n1 + n2
        print('')
        print('Calculando a \033[36msoma\033[m entre {} e {}...'.format(n1, n2))
        sleep(1)
        print('{:.0f} + {} = \033[36m{:.0f}\033[m'.format(n1, n2, soma))
        print('')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    elif menu == 2:
        multiplicar = n1 * n2
        print('')
        print('Calculando a \033[32mmultiplicaçao\033[m entre {} e {}...'.format(n1, n2))
        sleep(1)
        print('{} x {} = \033[32m{:.2f}\033[m'.format(n1, n2, multiplicar))
        print('')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    elif menu == 3:
        print('Calculando qual é o \033[33mmaior\033[m entre {} e {}'.format(n1, n2))
        sleep(1)
        if n1 > n2:
            maior = n1
            print('')
            print('Achei! O numero \033[33m{}\033[m é o maior'.format(maior))
            print('')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        else:
            maior = n2
            print('')
            print('Achei! O numero \033[33m{}\033[m é o maior'.format(maior))
            print('')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    elif menu == 4:
        print('')
        print('Por favor digite \033[34mnovos numeros\033[m ⤵')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
        print('')
        print('Atualizando o programa com os \033[34mnovos numeros\033[m...')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        sleep(0.5)
print('\033[31mSaindo do programa\033[m...')
sleep(1)
print('')
print('\033[35mObrigada por utilizar nosso programa!\033[m ')
print('┈┈┈┈╭╮╭╮\n'
'┈┈┈┈┃┃┃┃\n'
'┈┈┈┈┃┃┃┃\n'
'┈┈┈┈┃┗┛┣┳╮\n'
'┈┈┈╭┻━━┓┃┃\n'
'┈┈┈┃╲┏━╯┻┫\n'
'┈┈┈╰╮╯┊┊╭╯\n')