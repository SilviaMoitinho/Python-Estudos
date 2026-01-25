'''
Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execuçao, mostre a média entre todos os valores e
qual foi o maior e o menor valor lido. O prorama deve
perguntar ao usuario se ele quer ou nao continuar a digitar valores
'''

print('Média, Maior e menor')
print('')
n = int(input('Digite um numero -> '))
r = 'S'
maior = n
menor = n
cont = 0
soma = 0

while r == 'S':
    cont += 1
    soma += n
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r =='S':
        n = int(input('Digite um numero -> '))

media = soma/cont
print('Voce digitou {} valores, e a média deles é de {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
