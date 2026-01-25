"""
Crie um programa que leia o nome da pessoa
e diga se ela tem 'Silva' no nome
"""

nome = input('Digite o seu nome completo: ')

silva = nome.upper()
s = 'SILVA' in silva
print ('Seu nome tem Silva? {}'.format(s))