'''
Faça um programa que tenha uma funçao chamada maior(),
que receba varios parametros com valores inteiros. Seu
programa tem que analisar todos os valores e dizer qual
deles é o maior
'''

def maior(n):
    print('-='*30)
    print('Analisando os valores digitados.')
    cont = maior = 0
    for c in range(0, len(n)):
        print(f'{n[c]} ', end='')
        if cont == 0 or n[c] > maior:
            maior = n[c]
        cont += 1
    print(f'Foram informados {len(n)} numeros ao todo.')
    print(f'O maior valor informado foi {maior}')


valores = []

while True:
    v = int(input('Digite um numero (999 para parar): '))
    if v == 999:
        break
    valores.append(v)
maior(valores)