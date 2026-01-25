'''
Faça um programa que jogue par ou impar com o computador.
O jogo sera interrompido quando o jogador perder, mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo
'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('Deu par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente!')
print('Game Over!')
print(f'Voce ganhou {v} vezes')