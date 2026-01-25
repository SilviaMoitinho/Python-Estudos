'''
Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso crie duas listas extras, que vao conter apenas valores pares
e os valores impares respetivamente. No final, mostre o conteudo das 3
listas geradas.
'''

valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
for c in range(len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print('-'*30)
print(f'Os valores digitados foram {sorted(valores)}')
print(f'Os numeros pares: {pares}')
print(f'Os numeros impares: {impares}')