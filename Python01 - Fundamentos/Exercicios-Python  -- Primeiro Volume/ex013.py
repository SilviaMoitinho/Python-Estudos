salario = float(input('Qual é o salario do funcionario? R$'))
novo = salario + (salario*15 / 100)
print ('Um funcionario que ganhava R${}, com 15 por cento de aumento, passa a receber R${}'.format(salario, novo))