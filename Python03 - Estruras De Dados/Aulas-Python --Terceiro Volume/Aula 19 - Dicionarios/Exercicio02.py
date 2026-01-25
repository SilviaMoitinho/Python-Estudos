'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em
ordem, sabendo que o vencedor tirou o maior numero
'''

from random import randint
from time import sleep
cont = 1
dado = {'jogador1': randint(1,6),'jogador2': randint(1,6),
        'jogador3': randint(1,6),'jogador4': randint(1,6)}
print('Valores gerados:')
for k,v in dado.items():
    sleep(1)
    print(f'O {k} tirou {v}')
sleep(1)
print('Ranking dos jogadores:')
for v in sorted(dado, key= dado.get, reverse=True):
    sleep(1)
    print(f'{cont}° O {v} com {dado[v]}')
    cont += 1