'''
Desenvolva um programa que leia o comprimento de 3 retas
e diga ao usuario se elas podem ou nao formar um triangulo
'''

print('Digite 3 valores e veja se eles formas um triangulo')
n1 = float(input('Primeiro numero: '))
n2 = float(input('Segundo numero: '))
n3 = float(input('Terceiro numero: '))

if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print('Pode formar um triangulo!')
else:
    print('Nao pode formar um triangulo.')