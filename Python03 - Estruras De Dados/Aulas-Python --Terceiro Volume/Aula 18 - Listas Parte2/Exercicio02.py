'''
Crie um programa onde o usuario possa digitar sete valores
numericos e cadastre-os em uma lista unica que mantenha separados
os valores pares e impares. No final, mostre os valores pares
e impares em ordem crescente.
'''

numeros = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores impares digitados foram {sorted(numeros[1])}')
