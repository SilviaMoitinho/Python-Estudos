'''
Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso sera guardado em um dicionario, incluindo
o total de gols feitos durante o campeonato
'''

jogador = {}
gols = []
tot = 0
jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
p = int(input('Quantas partidas ele jogou? '))
for c in range(0, p):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    tot += gols[c]
jogador['Gols'] = gols
jogador['Total'] = tot
print('-'*30)
print(jogador)
print('-'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*30)
for c in range(0, p):
    print(f'    -> Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {tot} gols.')