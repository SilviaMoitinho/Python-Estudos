'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que foi multado.
A multa vai custar R$7 por cada km/h acima do limite
'''

velocidade = float(input('A que velocidade o carro passou no radar? km/h'))
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print('Ultrapassou o limite de velocidade! \n O carro estava a {}km/h por isso pagara uma multa de R${}'.format(velocidade, multa))
else:
    print('O caro esta dentro da velocidade permitida!')
