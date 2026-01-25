'''
Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respetivas posiçoes na lista
'''

posiçoesmaior = []
posiçoesmenor = []
menor = maior = contadorM = contadorm = 0
valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um numero na posiçao {cont}: ')))
    if cont == 0 or valores[cont] < menor:
        menor = valores[cont]
    if cont == 0 or valores[cont] > maior:
        maior = valores[cont]

print('.'*30)
print('Voce digitou os valores: ', end='')

for v in valores:
    print(f'{v},', end='')
for cont in range(0,5):
    if valores[cont] == menor:
        posiçoesmenor.append(cont)
        contadorM += 1
    if valores[cont] == maior:
        posiçoesmaior.append(cont)
        contadorm += 1

print('')
print('-'*30)

if contadorM == 1:
    print(f'\nO maior valor digitado foi {maior} na posiçao: {posiçoesmaior}', end='')
    for p in posiçoesmaior:
        print(f'{p}.', end='')
elif contadorM > 1:
    print(f'\nO maior valor digitado foi {maior} nas posiçoes: ', end='')
    for p in posiçoesmaior:
        print(f'{p}...', end='')
if contadorm == 1:
    print(f'\nO menor valor digitado foi {menor} na posiçao: {posiçoesmenor}', end='')
elif contadorm > 1:
    print(f'\nO menor valor digitado foi {menor} na posiçao: ', end='')
    for p in posiçoesmenor:
        print(f'{p}...', end='')