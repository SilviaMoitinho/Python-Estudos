#Estrutura Condicional Simples (nao tem else)
'''nome = str(input('Qual o seu nome?'))
if nome == 'Silvia':
    print('Que nome lindo que voce tem!')
print('Bom dia {}!'.format(nome))'''

#Estrutura Condicional Composta
'''nome = str(input('Qual o seu nome?'))
if nome == 'Silvia':
    print('Que nome lindo voce tem')
else:
    print('Seu nome é comum')
print('Bom dia, {}!'.format(nome))'''

#Verificando se foi uma media boa ou ruim com estrutras condicionais
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi de {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
