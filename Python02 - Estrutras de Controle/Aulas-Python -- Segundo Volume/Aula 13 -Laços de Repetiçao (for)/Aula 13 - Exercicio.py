'''
Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final mostre os 10 primeiros termos dessa progressao.
'''

n = int(input('Escolha um numero para começar a sua PA? '))
razao = int(input('Razao: '))
calculo = n + (10 - 1)*razao
for c in range(n,calculo+1, razao):
   print('{}'.format(c), end=' -> ')
print('FIM')