'''
Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
a) Quantos numeros foram digitados
b) A lista de valores, ordenada de forma descrescente
c) Se o valor 5 foi digitado e esta na lista ou nao
'''

n = []
cont = 0
while True:
    n.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
print(f'Foram digitados {len(n)} valores')
print(f'Lista de ordenada de forma decrescente: {sorted(n, reverse=True)}')
if 5 in n:
    print('O valor 5 esta na lista')
else:
    print('Nao existe o valor 5 na lista')