'''
Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

from funçoes import leia

i = leia.leiaInt('Digite um valor inteiro: ')
f = leia.leiaFloat('Digite um valor float: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')