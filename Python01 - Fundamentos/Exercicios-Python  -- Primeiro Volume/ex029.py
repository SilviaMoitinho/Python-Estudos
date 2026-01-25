'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que foi multado.
A multa vai custar R$7 por cada km/h acima do limite
'''

velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')