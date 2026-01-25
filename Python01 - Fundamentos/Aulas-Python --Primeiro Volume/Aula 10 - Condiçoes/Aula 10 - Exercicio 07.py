'''
Escreva um programa que pergunte o salario de um funcionario
e calcule o valor do seu aumento.
Para salarios superiores a R$1.250 calcule um aumento de 10%
para salarios inferiores ou iguais o aumento é de 15%
'''

sal = float(input('Qual o seu salario atual: R$'))
if sal <= 1250:
    a1 = sal + (sal * 15 / 100)
    print('Voce recebera 15%, de aumento! o seu novo salario é de R${}'.format(a1))
else:
    a2 = sal + (sal * 10 / 100)
    print('Voce recebera 10%, de aumento! Seu novo salario é de R${}'.format(a2))