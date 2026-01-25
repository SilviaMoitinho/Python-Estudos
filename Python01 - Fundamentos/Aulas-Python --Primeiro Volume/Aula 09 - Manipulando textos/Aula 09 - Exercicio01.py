"""
Crie um programa que leia o nome da pessoa e mostre:
- Nome em maiusculas
- Nome em minusculas
- Quantos caracteres tem o nome (sem contar os espaços)
- Quantas letras tem o primeiro nome
"""

nome = input('Digite o seu nome completo:')

nomema = nome.upper()
print('Seu nome em Maiusculas: {}'.format(nomema))

nomemi = nome.lower()
print('Seu nome em minusculas:{}'.format(nomemi))

semespaço = nome.replace(' ', '')
print('Seu nome tem ao todo {} letras'.format(len(semespaço)))

dividir = nome.split()
print('Seu primeiro nome é {} tem {} letras'.format(dividir[0],len(dividir[0])))