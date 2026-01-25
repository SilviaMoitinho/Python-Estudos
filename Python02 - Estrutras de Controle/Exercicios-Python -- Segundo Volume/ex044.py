'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e metodo de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- Em até 2x no cartao: Sem juros
- Em até 3x no cartao: 20% de juros
'''

print('{:=^40}'.format(' Lojinha '))
preço = float(input('Preço das compras: R$'))
print('''Forma de Pagamento
[1] à vista cheque/dinheiro
[2] à vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opçao = int(input('Qual é a opçao? '))

if opçao == 1:
    total = preço - (preço*10/100)
elif opçao == 2:
    total = preço - (preço*5/100)
elif opçao == 3:
    total = preço
    parcelas = preço/2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcelas))
elif opçao == 4:
    total = preço + (preço*20/100)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total/totparc
    print('Sua compra sera parcelada em {}x de R${:.2f}'.format(totparc, parcelas))
else:
    total = preço
    print('Opçao invalida de pagamento. Tente novamente')

print('Sua compra de R${} vai custar R${:.2f} no final'.format(preço, total))
