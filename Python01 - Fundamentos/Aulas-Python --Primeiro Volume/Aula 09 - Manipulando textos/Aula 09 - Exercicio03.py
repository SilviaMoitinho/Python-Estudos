""""
Crie um programa que leia um nome de uma cidade
e diga se ela começa com "Santo" ou nao
"""

cidade = input('Nome da cidade: ')

santo = cidade.upper().split()
s = 'SANTO' in santo[0]
print(s)