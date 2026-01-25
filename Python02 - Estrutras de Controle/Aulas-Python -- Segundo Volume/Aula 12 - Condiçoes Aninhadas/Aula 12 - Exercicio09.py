'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e metodo de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- Em até 2x no cartao: Sem juros
- Em até 3x no cartao: 20% de juros
'''
from time import sleep

print('~'*20)
print('Checkout')
preço = float(input('Valor do produto: R$'))
print('~'*20)
print('Modo de Pagamento')
print('[ 1 ] A vista dinheiro/cheque, Desconto de 10%')
print('[ 2 ] A vista no cartao, Desconto de 5%')
print('[ 3 ] No cartao até 2x, Sem Juros')
print('[ 4 ] No cartao até 3x, Juros de 20%')
print('[ 5 ] Cancelar a compra')
escolha = int(input('-> '))

if escolha == 5:
    print('Cancelando a sua compra...')
    sleep(2)
    print('Compra cancelada com Sucesso!')

if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
    print('Fatura para pagamento:')
    print('Produto: R${}'.format(preço))
    if escolha == 1:
        print('Desconto 10%')
        print('Valor a pagar: R${}'.format(preço - (preço*10/100)))
        print('Voce tem até 30 dias uteis para realizar o pagamento')
    elif escolha == 2:
        print('Desconto 5%')
        print('Valor a pagar: R${}'.format(preço - (preço*5/100)))
        print('Voce tem até 30 dias uteis para realizar o pagamento')
    elif escolha == 3:
        print('Juros 0%')
        print('Valor a pagar: R${}'.format(preço))
        print('Voce tem até 30 dias uteis para realizar o pagamento')
    elif escolha == 4:
        print('Juros 20%')
        print('Vaor a pagar: R${}'.format(preço + (preço*20/100)))
        print('Voce tem até 30 dias uteis para realizar o pagamento')

print('Tenha um BOM DIA!')