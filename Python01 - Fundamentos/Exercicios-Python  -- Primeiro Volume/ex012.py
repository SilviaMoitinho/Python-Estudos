preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço*5 / 100)
print ('O produto que custava R${}, na promoçao com 5 por cento de desconto vai custar R${}'.format(preço, novo))