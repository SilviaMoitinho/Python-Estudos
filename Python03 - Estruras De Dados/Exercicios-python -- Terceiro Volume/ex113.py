'''
Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro valido.\033[m')
            continue #Para continuar o laço
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n
        

n1 = leiaInt('Digite um valor Inteiro: ')
n2 = leiaFloat('Digite um valor real:')
print(f'O valor digitado inteiro foi {n1} e o real {n2}')