'''
Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

menor_peso = 0
maior_peso = 0
for c in range(0,1):
        peso = float(input('Digite um peso em kg ->'))
        if peso != 0:
            menor_peso = peso
            maior_peso = peso
        elif peso == 0:
            menor_peso = peso
for c in range(0, 4):
    peso = float(input('Digite um peso em kg -> '))
    if peso < menor_peso:
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso

print('O menor peso registado foi -> {:.1f}'.format(menor_peso))
print('O maior peso registado foi -> {:.1f}'.format(maior_peso))
