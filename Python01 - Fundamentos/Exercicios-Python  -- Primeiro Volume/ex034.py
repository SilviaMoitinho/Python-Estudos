'''
Escreva um programa que pergunte o salario de um funcionario
e calcule o valor do seu aumento.
Para salarios superiores a R$1.250 calcule um aumento de 10%
para salarios inferiores ou iguais o aumento é de 15%
'''

salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O seu novo salario é de R${:.2f}'.format(novo))