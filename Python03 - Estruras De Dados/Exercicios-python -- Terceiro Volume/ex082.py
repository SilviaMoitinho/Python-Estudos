'''
Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso crie duas listas extras, que vao conter apenas valores pares
e os valores impares respetivamente. No final, mostre o conteudo das 3
listas geradas.
'''

pares = list()
impares = list()
num = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
