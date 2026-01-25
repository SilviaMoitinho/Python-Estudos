'''
Escreva um programa que leia um numero inteiro qualquer e peça
para o usario escolher qual sera a base de conversao:
1 - para binario
2 - para octal
3 - para hexadecimal
'''

print('\033[36m-\033[m'*40)
print('Bem vindo ao Conversor Python!')
print('\033[36m-\033[m'*40)
n = int(input('Qual numero voce quer converter?'))
print('\033[36m-\033[m'*40)
print('MENU')
print('Escolha a opçao que deseja para converter o numero {}'.format(n))
print('\033[31m[ 1 ]\033[m - Binario')
print('\033[35m[ 2 ]\033[m - Octal')
print('\033[32m[ 3 ]\033[m - Hexadecimal')
escolha = int(input('-> '))
if escolha == 1:
    print('{} para BINARIO -> \033[31m{}\033[m'.format(n, (bin(n)[2:]))) #Converte um numero para binario
elif escolha == 2:
    print('{} para OCTAL -> \033[35m{}\033[m'.format(n, (oct(n)[2:]))) #Converte um numero para octal
else:
    print('{} para HEXADECIMAL -> \033[32m{}\033[m'.format(n, (hex(n)[2:]))) #Converte um numero para hexadecimal
print('Obrigada por escolher o Conversor Python!')
