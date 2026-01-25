'''
Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
O programa vai perguntaro casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestaçao mensal,sabendo que ela nao pode exceder 30% do salario
ou entao o emprestimo sera negado
'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamanto?'))
prestaçao = casa / (anos*12)
minimo = salario*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='') # end='' faz com que este print e o proximo apareçam na mesma linha
print(' a prestaçao sera de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')