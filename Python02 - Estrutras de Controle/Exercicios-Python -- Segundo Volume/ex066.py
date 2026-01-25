'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar 999, que é 
a condiçao de parada. No final, mostre quantos numeros foram digitados 
e qual foi a soma entre eles (desconsiderando o flag)
'''
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')