'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999,
que é a condiçao de parada. No final, mostre quantos numeros forma digitados 
e qual foi a soma deles (desconsiderando o flag)
'''

cont = soma = 0 # Podemos atribuir na mesma linha varias variaveis, se elas estiverem a receber o mesmo
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros'.format(cont))
print('A soma entre eles foi {}'.format(soma))
