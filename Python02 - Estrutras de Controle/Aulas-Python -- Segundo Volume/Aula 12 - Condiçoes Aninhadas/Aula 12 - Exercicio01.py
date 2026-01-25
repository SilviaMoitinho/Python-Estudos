'''
Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
O programa vai perguntaro casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestaçao mensal,sabendo que ela nao pode exceder 30% do salario
ou entao o emprestimo sera negado
'''

print('-=-'*20)
print('Financie a sua casa \033[31m SEM JUROS! \033[m \033[32m Crédito de 100% \033[m')
print('-=-'*20)

casa = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o seu salario atual? R$'))
anos = int(input('Por quantos anos voce quer financiar? '))
valor_prestaçao = casa / (anos*12)

if valor_prestaçao > (salario * 30 /100):
    print('\033[37;41m FINANCIAMENTO NEGADO! \033[m Para os parametros que indicou, nao consiguimos fazer o financiamento!')
elif valor_prestaçao <= (salario * 30/100):
    print('\033[32m Parabens! \033[m Voce pode financiar a sua casa \033[37;42m SEM JUROS! Com crédito de 100% \033[m')
    print('A sua prestaçao sera de \033[33m R${:.2f} \033[m por mes, durante {} anos ({} meses)'.format(valor_prestaçao, anos, anos*12))