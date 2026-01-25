'''
Faça um programa que tenha uma funçao chamada ficha(),
que receba 2 parametros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa devera ser capaz de
mostrar a ficha do jogador, mesmo que algum dado nao tenha
sido informado corretamente.
'''

def ficha(jog='desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


#Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Numerod de Gols: '))
if g.isnumeric(): #Para descobrir se a variavel é um numero
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n,g)