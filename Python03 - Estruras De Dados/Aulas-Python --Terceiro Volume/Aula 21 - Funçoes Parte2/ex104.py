'''
Crie um programa que tenha a funçao leiaInt(), que vai
funcionar de forma semelhante à funçao input() do Python,
so que fazendo a validaçao para aceitar apenas um valor numerico.
'''

def leiaInt(n):
    while True:
        try:
            n = int(input('Digite um numero: '))
            s = True
        except ValueError:
            print('\033[31mErro! Digite um numero inteiro valido\033[m')
            s = False
        if s == True:
            break
    return n


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
