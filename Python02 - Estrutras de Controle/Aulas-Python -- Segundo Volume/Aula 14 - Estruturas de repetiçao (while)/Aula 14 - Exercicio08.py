'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999,
que é a condiçao de parada. No final, mostre quantos numeros forma digitados 
e qual foi a soma deles (desconsiderando o flag)
'''

print('\033[31m⚠︎\033[m Se quiser pausar a soma digite \033[4;33m999\033[m \033[31m⚠︎\033[m')
print('')
print('↳ Soma de numeros com Python')
print('')
cont = 0
soma = 0
numero = 0
n = int(input('Digite um numero: '))

while n != 999:
    if n != 999:
        cont += 1
        soma += n
    else: 
        break
    n = int(input('Digite um numero: '))

print('No total voce digitou {} numeros'.format(cont))
print('E a soma entre eles é de {}'.format(soma))