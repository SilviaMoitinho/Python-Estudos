'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguntar se o usuario vai continuar ou nao.
No final, mostre:
a) Qual é o gasto total na compra
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato
'''

total = totmil = menor = cont = 0
barato =''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')