'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguntar se o usuario vai continuar ou nao.
No final, mostre:
a) Qual é o gasto total na compra
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato
'''

from time import sleep

print('\033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m•\033[m')
print('  Bem-vindo à Lojinha Pity')
print('\033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m• \033[33m• \033[32m•\033[m')
print('')
total = caro = cont = maisbarato = 0
nomebarato = ''

while True:
    cont += 1
    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    total += preço
    print('')
    print('Adicionando ao carrinho... 🛒')
    sleep(1)
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < maisbarato:
        maisbarato += preço
        nomebarato = nome
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break
    print('-'*30)
print('*'*30)
print('')
print('\033[32mFinalizando sua compra...\033[m ⏳')
sleep(2)
print('✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏')
print(f'Total da compra: \033[4;32mR${total}\033[m')
if caro == 1:
    print(f'\033[31m{caro}\033[m produto custa mais de \033[31mR$1000\033[m')
else:
    print(f'\033[31m{caro}\033[m produtos custam mais de \033[31mR$1000\033[m')
print(f'O produto mais barato é: \033[33m{nomebarato}\033[m custando \033[33mR${maisbarato}\033[m')