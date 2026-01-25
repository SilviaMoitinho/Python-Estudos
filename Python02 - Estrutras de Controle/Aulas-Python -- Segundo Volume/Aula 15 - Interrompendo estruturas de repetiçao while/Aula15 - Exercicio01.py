'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar 999, que é 
a condiçao de parada. No final, mostre quantos numeros foram digitados 
e qual foi a soma entre eles (desconsiderando o flag)
'''

n = soma = cont =0
while True:
    n = int(input('Digite um valor [\033[31m999\033[m para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
if cont == 1:
    print(f'Voce digitou apenas 1 valor -> \033[32m{soma}\033[m')
else:
    print(f'Voce digitou \033[1m{cont}\033[m valores e a soma entre eles é \033[32m{soma}\033[m')