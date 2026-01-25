'''
Desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem , cobrando R$0.50 por km
para viagens de até 200km e R$0.45 para viagens mais longas
'''

print('Calcule o preço da sua viagem')
d = float(input('Qual a distancia da sua viagem: km'))
if d > 200:
    p1 = 0.45 * d
    print('A sua viagem de {}km ficara por R${}'.format(d,p1))
else:
    p2 = 0.50 * d
    print('A sua viagem de {}km ficara por R${}'.format(d,p2))