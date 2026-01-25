'''
Faça um programa que tenha uma funçao chamada ficha(),
que receba 2 parametros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa devera ser capaz de
mostrar a ficha do jogador, mesmo que algum dado nao tenha
sido informado corretamente.
'''


def ficha(n, g):
    if n == '':
        n = 'desconhecido'
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Numero de  gols: ')
ficha(nome, gols)
