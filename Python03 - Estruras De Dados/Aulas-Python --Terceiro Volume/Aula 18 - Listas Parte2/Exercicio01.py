'''
Faça um programa que leia o nome e o peso, de varias pessoas, guardando tudo
em uma lista. No final, mostre:
a) Quantas pessoas foram registradas
b) Uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
'''

pessoas = []
dados = []
maisp = menosp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maisp = menosp = dados[1]
    else:
        if dados[1] > maisp:
            maisp = dados[1]
        if dados[1] < menosp:
            menosp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('-'*30)
print(f'No total foram resgistradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maisp:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maisp:
        print(f'{p[0]}...', end='')
print()
print(f'O menor peso doi de {menosp:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menosp:
        print(f'{p[0]}...', end='')